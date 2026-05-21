""" Chapter 03: Descriptive and Inferential Statistics (Contd.)"""
# Contiune...

""" 1. Z-Scores """
# Expresses all x-values in terms of standard deviations.
# Turning an x-value into a Z-score uses a basic scaling.

# z = x - mu / o

# Neightborhood A, has a mean home value of 140,000 and standard deviation of 3000
# mu(A) = 140,000 and o(A) = 3,000 
# 4.1: Turn Z-score into x-values and vice versa
def z_score(x, mean, std):
  
  return (x - mean) / std
def z_to_x(z, mean, std):
    return (z * std) + mean

mean = 140000
std_dev = 3000
x = 150000

# Convert to Z-score and then back to X
z = z_score(x, mean, std_dev)
back_to_x = z_to_x(z, mean, std_dev)
print("Z-Score: {}".format(z)) # Z-Score: 3.333
print("Back to X: {}".format(back_to_x)) # Back to X: 150000.0

""" 2. Inferential Statistics """
# Sample and population come into full play
# Slow down You can't judge it quickly with this one.

""" 3. ** The Central Limit Theorem """
# Exploring the central limit theorem in Python

# 4.2: Samples of the uniform distribution will average out to a normal distribution.
import random
import plotly.express as px

sample_size = 31
sample_count = 1000

# Central limit theorem, 1000 samples each with 31
# random numbers between 0.0 and 1.0
x_values = [(sum([random.uniform(0.0, 1.0) for i in range(sample_size)]) / \
    sample_size)
        for _ in range(sample_count)]

y_values = [1 for _ in range(sample_count)]

px.histogram(x=x_values, y = y_values, nbins=20).show()

# Sample Standard Deviation = Population Stanard Deviation / Sqrt(Sample_Size)
# How much Sample is enough?
# 31 is the magic number that you need in a sample to satisfy the central limit theorem and see a normal disttribution

""" 4. ** Confidence Intervals """
# a range calculation showing how confidently we believe a sample mean
# LOC, Level of confidence = contain the desired probability for the population mean range

# 4.3: Retrieving a critical z-value
from scipy.stats import norm

def critical_z_value(p):
   norm_dist = norm(loc=0.0, scale=1.0)
   left_tail_area = (1.0 - p) / 2.0
   upper_area = 1.0 - ((1.0 - p)) / 2.0
   return norm_dist.ppf(left_tail_area), norm_dist.ppf(upper_area)

print(critical_z_value(p=0.95)) # +-1.95996

# E = margin of error = the range around the sample mean that contains the population mean at that level of confidence
# Apply that margin of error against the sample mean = get the confidence interval

# 4.4: Calc. a confidence interval in Python
from math import sqrt
from scipy.stats import norm

def critical_z_value(p):
   norm_dist = norm(loc=0.0, scale=1.0)
   left_tail_area = (1.0 - p) / 2.0
   upper_area = 1.0 - ((1.0 - p) / 2.0)
   return norm_dist.ppf(left_tail_area), norm_dist.ppf(upper_area)

def confidence_interval(p, sample_mean, sample_std, n):
   # Sample size must be greater than 30

   lower, upper = critical_z_value(p)
   lower_ci = lower * (sample_std / sqrt(n))
   upper_ci = upper * (sample_std / sqrt(n))

   return sample_mean + lower_ci, sample_mean + upper_ci

print(confidence_interval(p=.95, sample_mean=64.408, sample_std=2.05, n=31))
# 63.68 & 65.12
# The larger n becomes the narrower our confidence interval becomes!

""" 5. ** P-Values """
# THe probability of something occuring by chance
# not because of a hypothesized explanation

# null hypothesis(h0) the variable in had no impact on the experiment, just random luck.
# alternative hypothesis(h1) the variable or controlled variable is causing a positive result

# 4.5 Hypothesis Testing
# Calc. the prob. of recovery between 15 and 21 days
from scipy.stats import norm

# Cold has 18 day mean recovery, 1.5 std_dev
mean = 18
std_dev = 1.5

# 95% prob. recovery time takes between 15 and 21 days
x = norm.cdf(21, mean, std_dev) - norm.cdf(15, mean, std_dev)

print(x) # 0.95 or 95% chance to recover within 15 and 21 days of cold
# also 2.5% chance of recover taking longer than 21 days, and 2.5% chance taking fewer than 15 days

# 4.6 One-Tailed Test
# getting x-value with 5% of area behind it
from scipy.stats import norm

# Cold has 18 day mean recovery, 1.5 std_dev
mean = 18
std_dev = 1.5

# what x-value has 5% of area behind it?
x = norm.ppf(.05, mean, std_dev)

print(x) # 15.532 day to recovey time
# but the sample mean is 16, so not fall into this null hypothesis and not a statistical significance test

# 4.7 Calc. the One-Tailed p-value
from scipy.stats import norm

# Cold has 18 day mean recovery, 1.5 std_dev
mean = 18
std_dev = 1.5

# Prob. of 16 or less day
p_value = norm.cdf(16, mean, std_dev)

print(p_value) # 0.091 it greater than .05 = not consider the drug trial a success and fail to rejet our null hypothesis

# 4.8 Two-Tailed Test
# frame our null and alternative hypothesis in an "equal" and "not-equal" structure
# spread our p-value threshold of both tails, not just one
# under or over? reject the null hypothesis
# Calc. a range for a statistical significance of 5%
from scipy.stats import norm

mean = 18
std_dev = 1.5

# what x-value has 2.5% of area behind it?
x1 = norm.ppf(.025, mean, std_dev)

# What x-value has 97.5% of area behind it
x2 = norm.ppf(.975, mean, std_dev)

print(x1) # 15.06
print(x2) # 20.93
# same mean value is 16, not less than 15.06 and not greater than 20.93
# we still fail to reject the null hypothesis...

# 4.9 Calc. the Two0Tailed p-value
from scipy.stats import norm

mean = 18
std_dev = 1.5

# Probability of 16 or less day
p1 = norm.cdf(16, mean, std_dev)

# Probability of 20 or more day
p2 = 1.0 - norm.cdf(20, mean, std_dev)

# P-value of both tails
p_value = p1 + p2

print(p_value) # 0.1824

""" 6. T-distribtion: Dealing with small samples """
# use this if we have a sample lower than 30
# just like normal distribution but has fatter tails to reflect more variance and undertanty
# The samller the sample size = the larger the range, reflecting greater uncertainty

# 4.10: find critical t-value of 95% with t-distribution
from scipy.stats import t

# critical value range for 95% confidence
# sample size of 25

n = 25
lower = t.ppf(.025, df=n-1)
upper = t.ppf(.975, df=n-1)

print(lower, upper) # -2.063, 2.063
# df = degree of freedom

# Texas sharpshooter Fallacy = Stumble on something rare and then point out, somehow create predictive values

# Try to use structured hypothesis testing and gather data for objective
# data mining = gathers data, then hypothesis
# Searching for patterns on raw data!
