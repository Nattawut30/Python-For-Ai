"""
Quick EDA — Run this BEFORE building the dashboard.
This is what you'd naturally do when you first get a dataset.
Run: python quick_eda.py
"""

import pandas as pd

df = pd.read_csv("02_saas_funnel_data.csv")

# ── 1. First look ──
print("=" * 60)
print("FIRST LOOK AT THE DATA")
print("=" * 60)
print(f"\nShape: {df.shape[0]} rows x {df.shape[1]} columns\n")
print(df.head(10).to_string())

# ── 2. Column types & nulls ──
print("\n" + "=" * 60)
print("DATA TYPES & MISSING VALUES")
print("=" * 60)
info = pd.DataFrame({
    "dtype": df.dtypes,
    "non_null": df.notna().sum(),
    "null": df.isna().sum(),
    "null_%": (df.isna().sum() / len(df) * 100).round(1)
})
print(f"\n{info.to_string()}")

# ── 3. Funnel stage distribution ──
print("\n" + "=" * 60)
print("WHERE ARE LEADS DROPPING OFF?")
print("=" * 60)
stages = df["current_stage"].value_counts()
print(f"\n{stages.to_string()}")
total = len(df)
print(f"\n  Lead → MQL:           {df['mql_date'].notna().sum():>5} ({df['mql_date'].notna().sum()/total*100:.1f}%)")
print(f"  MQL → Demo Booked:    {df['demo_booked_date'].notna().sum():>5} ({df['demo_booked_date'].notna().sum()/total*100:.1f}%)")
print(f"  Demo Booked → Done:   {df['demo_completed_date'].notna().sum():>5} ({df['demo_completed_date'].notna().sum()/total*100:.1f}%)")
print(f"  Demo → Trial:         {df['trial_start_date'].notna().sum():>5} ({df['trial_start_date'].notna().sum()/total*100:.1f}%)")
print(f"  Trial → Closed Won:   {len(df[df['current_stage']=='Closed Won']):>5} ({len(df[df['current_stage']=='Closed Won'])/total*100:.1f}%)")

# ── 4. Lead source breakdown ──
print("\n" + "=" * 60)
print("LEAD SOURCES — WHO BRINGS THE MOST?")
print("=" * 60)
print(f"\n{df['lead_source'].value_counts().to_string()}")

# ── 5. Quick cross-tab: source × stage ──
print("\n" + "=" * 60)
print("CROSS-TAB: SOURCE × FINAL STAGE")
print("=" * 60)
ct = pd.crosstab(df["lead_source"], df["current_stage"])
print(f"\n{ct.to_string()}")

# ── 6. Company size breakdown ──
print("\n" + "=" * 60)
print("COMPANY SIZE DISTRIBUTION")
print("=" * 60)
print(f"\n{df['company_size'].value_counts().to_string()}")

# ── 7. Revenue stats ──
print("\n" + "=" * 60)
print("REVENUE (closed deals only)")
print("=" * 60)
closed = df[df["deal_value"] > 0]
print(f"\n  Total deals closed:  {len(closed)}")
print(f"  Total revenue:       ${closed['deal_value'].sum():,.0f}")
print(f"  Avg deal size:       ${closed['deal_value'].mean():,.0f}")
print(f"  Median deal size:    ${closed['deal_value'].median():,.0f}")
print(f"  Largest deal:        ${closed['deal_value'].max():,.0f}")

# ── 8. Speed to demo ──
print("\n" + "=" * 60)
print("DAYS FROM MQL → DEMO BOOKING")
print("=" * 60)
speed = df["days_mql_to_demo_booked"].dropna()
print(f"\n  Count:   {len(speed)}")
print(f"  Mean:    {speed.mean():.1f} days")
print(f"  Median:  {speed.median():.1f} days")
print(f"  Max:     {speed.max():.0f} days")

# ── 9. Sales rep lead count ──
print("\n" + "=" * 60)
print("SALES REP — LEAD DISTRIBUTION")
print("=" * 60)
print(f"\n{df['sales_rep'].value_counts().to_string()}")

print("\n" + "=" * 60)
print("EDA DONE — now let's build the dashboard!")
print("=" * 60)
