"""
B2B SaaS Funnel Dashboard — Streamlit
Run: streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Config ──
st.set_page_config(page_title="SaaS Funnel Analytics", page_icon="🔍", layout="wide")

# ── Load data ──
@st.cache_data
def load_data():
    df = pd.read_csv("saas_funnel_data.csv", parse_dates=[
        "created_date", "mql_date", "demo_booked_date",
        "demo_completed_date", "trial_start_date", "closed_date"
    ])
    df["created_month"] = df["created_date"].dt.to_period("M").astype(str)
    return df

df = load_data()

# ── Sidebar filters ──
st.sidebar.title("🔍 Filters")

date_range = st.sidebar.date_input(
    "Date range",
    value=(df["created_date"].min(), df["created_date"].max()),
    min_value=df["created_date"].min(),
    max_value=df["created_date"].max(),
)

sizes = st.sidebar.multiselect("Company Size", df["company_size"].unique().tolist(), default=df["company_size"].unique().tolist())
reps = st.sidebar.multiselect("Sales Rep", df["sales_rep"].unique().tolist(), default=df["sales_rep"].unique().tolist())

fdf = df[
    (df["created_date"] >= pd.Timestamp(date_range[0])) &
    (df["created_date"] <= pd.Timestamp(date_range[1])) &
    (df["company_size"].isin(sizes)) &
    (df["sales_rep"].isin(reps))
].copy()

# ── Header + KPIs ──
st.title("📊 B2B SaaS Funnel Dashboard")
st.caption(f"Analyzing {len(fdf):,} leads from {date_range[0]} to {date_range[1]}")

won = fdf[fdf["current_stage"] == "Closed Won"]
churned = fdf[fdf["current_stage"] == "Churned"]
closed_total = len(won) + len(churned)

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Total Leads", f"{len(fdf):,}")
k2.metric("Closed Won", f"{len(won):,}")
k3.metric("Revenue", f"${fdf['deal_value'].sum():,.0f}")
k4.metric("Win Rate", f"{closed_total / len(fdf) * 100:.1f}%" if len(fdf) else "0%")
k5.metric("Churn Rate", f"{len(churned) / closed_total * 100:.1f}%" if closed_total else "0%")

st.divider()

# ── 1) Funnel ──
st.subheader("🔻 Full Funnel Breakdown")

funnel_stages = ["Lead", "MQL", "Demo Booked", "Demo Completed", "Trial Started", "Closed Won"]
funnel_counts = [
    len(fdf),
    fdf["mql_date"].notna().sum(),
    fdf["demo_booked_date"].notna().sum(),
    fdf["demo_completed_date"].notna().sum(),
    fdf["trial_start_date"].notna().sum(),
    closed_total,
]

fig_funnel = go.Figure(go.Funnel(
    y=funnel_stages, x=funnel_counts,
    textinfo="value+percent previous",
    marker=dict(color=["#4C78A8", "#54A24B", "#E45756", "#F58518", "#72B7B2", "#FF9DA6"]),
))
fig_funnel.update_layout(height=420, margin=dict(t=10, b=10))
st.plotly_chart(fig_funnel, use_container_width=True)

# ── 2) Company Size ──
st.subheader("🏢 Company Size: Volume vs. Close Rate")

size_order = ["Startup (1-10)", "SMB (11-50)", "Mid-Market (51-200)", "Enterprise (200+)"]
sz = fdf.groupby("company_size").agg(
    leads=("lead_id", "count"),
    wins=("current_stage", lambda x: x.isin(["Closed Won", "Churned"]).sum()),
).reindex(size_order)
sz["win_rate"] = (sz["wins"] / sz["leads"] * 100).round(1)

fig_sz = px.bar(sz, x=sz.index, y="leads", text="leads", title="Lead Volume & Win Rate by Company Size")
fig_sz.add_scatter(x=sz.index, y=sz["win_rate"], mode="lines+markers+text",
                   text=sz["win_rate"].astype(str) + "%", textposition="top center",
                   name="Win Rate %", yaxis="y2",
                   line=dict(color="#E45756", width=3), marker=dict(size=10))
fig_sz.update_layout(
    yaxis2=dict(title="Win Rate (%)", overlaying="y", side="right"),
    height=380, showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=1.02),
)
st.plotly_chart(fig_sz, use_container_width=True)

# ── 3) Speed to Demo ──
st.subheader("⏱️ Speed Kills: Days from MQL → Demo Booking")

speed_df = fdf[fdf["days_mql_to_demo_booked"].notna()].copy()
speed_df["speed"] = speed_df["days_mql_to_demo_booked"].apply(
    lambda x: "Fast (1-4 days)" if x <= 4 else "Slow (5+ days)"
)

col1, col2 = st.columns([1, 2])

# Summary table
summary = speed_df.groupby("speed").agg(
    Leads=("lead_id", "count"),
    Wins=("current_stage", lambda x: x.isin(["Closed Won", "Churned"]).sum()),
)
summary["Win Rate %"] = (summary["Wins"] / summary["Leads"] * 100).round(1)
col1.dataframe(summary, use_container_width=True)

# Histogram
fig_spd = px.histogram(
    speed_df, x="days_mql_to_demo_booked", color="current_stage",
    nbins=14, title="Distribution of Days MQL → Demo Booking",
    barmode="stack",
)
fig_spd.update_layout(height=350)
col2.plotly_chart(fig_spd, use_container_width=True)

# ── 4) Monthly Trend ──
st.subheader("📈 Monthly Funnel Trend")

monthly = fdf.groupby("created_month").agg(
    leads=("lead_id", "count"),
    wins=("current_stage", lambda x: x.isin(["Closed Won", "Churned"]).sum()),
).reset_index()
monthly["win_rate"] = (monthly["wins"] / monthly["leads"] * 100).round(1)
monthly["period"] = monthly["created_month"].apply(
    lambda m: "Q4" if any(q in m for q in ["2025-10", "2025-11", "2025-12"]) else "Other"
)

fig_trend = px.bar(monthly, x="created_month", y="leads", color="period",
                   color_discrete_map={"Q4": "#F6C343", "Other": "#4C78A8"},
                   title="Leads per Month (Q4 highlighted)")
fig_trend.add_scatter(x=monthly["created_month"], y=monthly["win_rate"],
                      mode="lines+markers", name="Win Rate %", yaxis="y2",
                      line=dict(color="#E45756", width=3), marker=dict(size=8))
fig_trend.update_layout(
    yaxis2=dict(title="Win Rate (%)", overlaying="y", side="right"),
    height=400, legend=dict(orientation="h", yanchor="bottom", y=1.02),
)
st.plotly_chart(fig_trend, use_container_width=True)

# ── Footer ──
st.divider()
st.caption("Built with Streamlit + Plotly · Data is synthetic · @loresowhat")
