"""Chapter 03: Descriptive and Inferential Statistics"""

# Statistics is important in AI/ML

# What is Data?
# The more data you have, the more you closer to the truth
# Data is not that important. Analysis data is.
# Data may be biased.
# Data does not capture context or explanations
# Data provides clues not truth. the clue that can lead us to the truth
# Keep asking questions how the data was created, by who?

# Garbage in, Garbae out
# only 13% ML projects succeed.
# Success ML = Doing a lot of data cleaning

# Descriptive Stats. = use it to summarize data
# Inferential Stats. = to uncover attributes based on a sample (less intuitive)
# A population = a particular group of interest we wanna study. Could be large, small, or specific
# A sample = a subset of the population that is ideally random and unbiased

# Data must be random and true. 
# Data bias is inevitable.

# ==============================================

""" 1. Data Bias Types """

# Human are always biased. (sad but true...)

# Confirmation bias = gathering only data that supports your belief (follwoing only celeb we likes and political our sides.)
# Self-selection bias = a certain types of subjects are include themselves in the experiment (Airlines arks customers who already get in the plane of that airline)
# Survival bias = catures only living, survived, and actived subjects. not care the dead one. (Fighter airplane WW2.)

# Reminders: Computer and math don't recognize the bias in the data. It's on you.
# Reminders: Data bias = ML algorithm makes biased conclusions.

# ==============================================

""" 2. Mean and Weighted Mean """

# Mean = the average of a set of values.
# Sum the values > Divide by the number of values
# Mean shows the "Center of gravity"

# 3.1: Calc. mean
# Number of pets each person owns
sample = [1, 3, 2, 5, 7, 0, 2, 3]
mean = sum(sample) / len(sample)

print(mean) # 2.875

# 3.2: Calc. a weighted mean (academic exam)
# 3 exams of .20 weight each and final exam of .40 weight
sample = [90, 80, 63, 87]
weights = [.20, .20, .20, .40]

weighted_mean = sum(s * w for s, w in zip(sample, weights)) / sum(weights)

print(weighted_mean) # 81.4

# 3.3: Calc. a weighted mean
# same sameple but use 1 for 20% and 2 for 40%
sample = [90, 80, 63, 87]
weights = [1.0, 1.0, 1.0, 2.0]

weighted_mean = sum(s * w for s, w in zip(sample, weights)) / sum(weights)

print(weighted_mean) # 81.4 same!

# ==============================================

""" 3. Median """
# The middlemost value in a set of ordered values.
# But already 'sequentially order the value'

# 3.4: Calc. the median
# Number of pets each person owns
sample = [0, 1, 5, 7, 9, 10, 14]

def median(values):
    ordered = sorted(values)
    print(ordered) # Sequentlly values

    n = len(ordered)
    mid = int(n / 2) - 1 if n % 2 == 0 else int(n / 2)

    if n % 2 == 0:
        return (ordered[mid] + ordered[mid+1]) / 2.0
    else:
        return ordered[mid]
    
print(median(sample)) # 7

# ==============================================

""" 4. Mode """
# The most frequently occuring in set of values
# Useful when data is very repetitive

# No value occurs more than once, no mode
# 2 values occur with an equal amount of frequency = the dataset is bimodal

# 3.5: Calc. the mode
# Number of pet each person owns, obvoiously bomodal 2 and 3
from collections import defaultdict

sample = [1, 3, 2, 5, 7, 0, 2, 3]

def mode(values):
    counts = defaultdict(lambda: 0)

    for s in values:
        counts[s] += 1

    max_count = max(counts.values())
    modes = [v for v in set(values) if counts[v] == max_count]
    return modes

print(mode(sample)) # [2, 3]

# ==============================================

""" 5. Variance and Standard Deviation """

# There are some cal culation differences for the sample versis the population.
# We could sum the absolute values by rid the negaative signs and make all values positive

# 3.6: Calc. variance in Python
# Number of pets each person owns
data = [0, 1, 5, 7, 9, 10, 14]

def variance(values):
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / len(values)
    return _variance

print(variance(data)) # 21.387

# 3.7: Calc. standard deviation
from math import sqrt

# Number of pets each person owns
data = [0, 1, 5, 7, 9, 10, 14]

def variance(values):
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / len(values)
    return _variance

def std_dev(values):
    return sqrt(variance(values))

print(std_dev(data)) # 4.62

# s^2 = ∑(xi - x_)^2 / n - 1
# s = sqrt[∑(xi - x_)^2 / n - 1]

# we divided 1 to avoid any bias in a sample!
# It's a sample not a populations

# 3.8: Calc. standard deviation for a sample
from math import sqrt

data = [0, 1, 5, 7, 9, 10, 14]

def variance(values, is_sample: bool = False):
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / (len(values) - (1 if is_sample else 0))

    return _variance

def std_dev(values, is_sample: bool = False):
    return sqrt(variance(values, is_sample))

print("VARIANCE = {}".format(variance(data, is_sample=True))) # 24.952380
print("STD_DEV = {}".format(std_dev(data, is_sample=True))) # 4.99523

# ==============================================

""" 6. ** The Normal Distribution """

# The Gaussian distribution
# Bell-shaped distribution
# heads - tails become thinner as you move away from the mean
# histograms helps more understanding
# Use it and represents daily life

# The Probability Density Funtion (PDF)
# it defines how spread out it is
# normal distribution, returns likelihood

# The Cumulative Distrivbution Funtion (CDF)
# CDF is an S-shaped curve called a sigmoid curve, 
# project the area up to that range in the PDF.

# 3.9: The normal distribution CDF in Python
from scipy.stats import norm

mean = 64.43
std_dev = 2.99

x = norm.cdf(64.43, mean, std_dev)

print(x) # 0.5

# 3.10: Getting a middle range probability
from scipy.stats import norm

mean = 64.43
std_dev = 2.99

x = norm.cdf(66, mean, std_dev) - norm.cdf(62, mean, std_dev)

print(x) # 0.49204 or 49.2% for a golden retriever between 62 and 66 pounds.

# ==============================================

""" 7. The Inverse CDF """


# backward' em.
# let's find the weight that 95% of golden retrivers
# 3.11: The inverse CDF
from scipy.stats import norm

weight = norm.ppf(.95, loc=64.43, scale=2.99)
print(weight)
# so 95% of golden retrivers are 69.348 or fewer pounds.


# 3.12: Generateting random numbers from a normal distribution
import random
from scipy.stats import norm

for i in range(0, 1000):
    random_p = random.uniform(0.0, 1.0)
    random_weight = norm.ppf(random_p, loc=64.43, scale=2.99)
    print(random_weight)