""" Chapter 02: Probability """

# 0% - 100% = 0.0 - 1.0 formats
# P(X) = .70 = 70%

# Probability = predictions of events yet to happen
# Likelihood = measuring the frequency of events that already occured

# Collecting data is the only way to discover the probability

# Fraction = Up(Cardinal) / Down(Ordinal)

# ==============================================

""" 1. JOINT """
# AND = Multiplying

# P(A AND B) = P(A) X P(B)
# P(heads) = 1 / 2 (coin)
# P(6) = 1 / 6 (die)
# P(heads AND 6) = 1 / 2 * 1 / 6 => 1 / 12, .08333

# ==============================================

""" 2. UNION """
# OR = Plus add them together

# P(4) = 1 / 6
# P(6) = 1 / 6
# P(4 OR 6) = 1 / 6 + 1 / 6 = 2 / 6 => 1 / 3 # Cut minimal

# P(heads) = 1 / 2
# P(6) = 1 / 6
# P(heads OR 6) = 1 / 2 + 1 / 6 = 4 / 6 = .666

# Reminder: MUST BE NO MORE THAN 100% or 1.0

# Sum rule of probability
# P(A OR B) = P(A) + P(ฺB) - P(A) * P(B)

# What's the prob of a heads or a 6? (subtract the joint the prob of getting a heads or a 6)

# P(heads) = 1 / 2
# P(6) = 1 / 6
# P(heads or 6) = (1 / 2 + 1 / 6) - (1 / 2 * 1 / 6) 
# = (4 / 6) - (1 / 12) = Below must be equal 7 / 12 = .58333

# ==============================================

""" 3. Conditional Probability + Bayes' Theorem """

# Event A occurring given event B has occured.
# P(A GIVEN B) or P(A|B)

# P(Coffee given Cancer) or P(Coffee|Cancer)
# Direction matters!

# P(Coffee) = .65
# P(Cancer) = .005
# P(Coffee|Cancer) = .85
# Few coffee drinkers have cancer, but many cancer patients drink coffee.

# 2.1:
# Flip conditional prob (Bayes's Theorem)
# P(A|B) = P(B|A) * P(A) / P(ฺB)
# P(Cancer|Coffee) = P(Coffee|Cancer) * P(Cancer) / P(Coffee)
# P(Cancer|Coffee) = 0.85 * 0.05 / 0.65 = 0.0065

p_coffee_drinker = .65
p_cancer = .005
p_coffee_drinker_given_cancer = .85

p_cancer_given_coffee_drinker = p_coffee_drinker_given_cancer * p_cancer / p_coffee_drinker

print(p_cancer_given_coffee_drinker) # 0.0065 ...

# Answer: The prob someone has cancer given they are a coffee drinker is only 0.65%

# ==============================================

""" 4. Joint and Union Conditional Probabilities """

# Find the prob somebody is a coffee drinker AND they have cancer.
# One is more specific and applies to a condition that's already been established
# P(Coffee and Cancer) = P(Coffee|Cancer) * P(Cancer)
# = 0.85 * 0.005 = 0.00425

# Joint prob if the 2 events are dependent
# P(A AND B) = P(B) * P(A|B)

# Union prob if A or B occurring but A may affect the prob of B
# P(A OR B) = P(A) + P(B) - P(A|B) * P(B)

# ==============================================

""" 5. Binomial and distributions """

# The only way we will know for sure is to run more tests
# binomial distribution = how likely 'k' successes can happen out of 'n' trials given 'p' probability

# 2.2: 
# SciPy for the binomial distribution
from scipy.stats import binom

n = 10
p = 0.9

for k in range(n + 1):
    probability = binom.pmf(k, n, p) # PMF = probability mass function
    print("{0} - {1}".format(k, probability))

# n = the number of trials
# p = the probability of success for each trial
# k = the number of sucesses we wanna look up the probability for

# ==============================================

""" 6. Beta Distribution """

# Allos us to see the likelihood of different underlying probabilities for an event to occur 
# Given alpha suceesses and beta failures

# X-axis = all underlying reates of success from 0.0 to 1.0
# Y-axis = the likelihood of that probability
# The beta distribution allows us to ee the probabilities of probabilities given 8/10 successes

# CDF = cumulative density function

# 2.3:
# Beta distribution using SciPy - Calc. the area up to 90%
from scipy.stats import beta

a = 8
b = 2

p = beta.cdf(.90, a, b)

print(p) # 77.48% chance the underlying probability of success is 90% or less.

# a = the number of successes
# b = the number of failures
# the underlying probability of success rate

# ** CDF calculates area only to the left of our boundary, not the right!

# 2.4:
# Substracting to get a right area in a beta distribution
from scipy.stats import beta

a = 8
b = 2

p = 1.0 - beta.cdf(.90, a , b)

print(p)

# out of 8/10 successful tests, there's only 22.5% chance the underlying success rate is 90% or greater
# but there's 77.5% chance it is less than 90%

# 2.5:
# a beta distribtution with more trials - Granted more test up to 30
from scipy.stats import beta

a = 30
b = 6

p = 1.0 - beta.cdf(.90, a, b)

print(p)
# Good idea to walk away now
# unless you wanna bet agaist this 13.16% chance like this!

# 2.6:
# middle area beta distributions using SciPy
# what % chance between 80% - 90% success rate?
from scipy.stats import beta

a = 8
b = 2

p = beta.cdf(.90, a, b) - beta.cdf(.80, a, b)

print(p)
# Success rate of 80% - 90% have a chance of 33.86% to get here. wanna bet?

# Concluded:
# 1. It allows us to reason about probabilities of probabilites, and we can update it as we get a new data
# 2. calculate the alpha or the left as a main
# 3. use it for hypothesis testing
# 4. Tests more to find a chance
# 5. It's about finding the underlying