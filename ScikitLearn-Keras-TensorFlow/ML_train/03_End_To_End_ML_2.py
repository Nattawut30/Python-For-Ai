""" Chapter 02: End-To-End Machine Learning Project (Contd.) """

""" 1. Create a Test Set """

# Your brain is capable of scanning data at glance btw
# Data snooping bias = you estimate the general error using the test set, it usually optimmistic, and will lanuch a system that not perform well

# Create a test set: pick instances randomly, typically 20% of the dataset or less it your dataset is very large

import numpy as np

def shuffle_and_split_data(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size]
    return data.iloc[train_indices], data.iloc[test_indices]

# Call the funciton like this:
# train_set, test_set = shuffle_and_split_data(housing, 0.2)
# len(train_set)
# len(test_set)

# Good but not best... if you run the program again, it will generate a different test set!

# Solutions:
# 1. save the test set on the first run and then load it in subsequent runs
# 2. Set the random number generator's seed, so that it always generates the same shuffled indices (np.random.seed(42), np.random.permutation())

# Best solutions for a stable train/test split even after updating the dataset:
# - use each instance's identifier to decide whether or not it should go in the test set

# (you will see people set the random seed to 42. Don't mean anything, but use it)

from zlib import crc32

def is_id_in_test_set(identifier, test_ratio):
    return crc32(np.int64(identifier)) < test_ratio * 2**32

def split_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

# If your dataset does not have "identifier column" use the row index as the ID:

# housing_with_id = housing.reset_index() | # Adds an 'index' column
# train_set, test_set = split_data_with_id_hash(housing_with_id, 0.2, "index")

# Make sure the new data gets appended to the end of the dataset and that no row ever gets deleted.
# Not possible? try to use the most stable features t o build a unique identifier.

# Scikit-Learn provides a few functions to split dataset into multiple subsets in various ways
# train_test_split()

# random_state parameter allows you to set the random generator seed
# pass it multiple datasets with identical number of rows, it will split them on the same indices

# from sklearn.model_selection import train_test_split
# train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

# if your dataset is large enough = fine
# if not, you run the risk of introducing a significant sampling bias

# "Stratified Samping" = make an assumptions for the data survey female 51.1% and male 48.9%: 511 females and 489 males
# The population is divided into homogenous subgroups called "strata"

# Use pd.cut() function to create the category attribute with 5 categories
# Scikit-Learn provides a number of splitter classes in the sklearn.model_selection package

# The split() method yields the training and test indices not the data itself
from sklearn.model_selection import StratifiedShuffleSplit

splitter = StratifiedShuffleSplit(n_splits=10, test_size=0.2, random_state=42)
strat_splits = []

# First split
strat_train_set, strat_test_set = strat_splits[0]

# train_test_split() with the stratify arfguments works too!

# Looking at proportions in the test set:
strat_test_set["income_cat"].value_counts() / len(strat_test_set)

# drop income_cat column and reverting the data back to the original state:
for set_ in (strat_train_set, strat_train_set):
    set_.drop("income_cat", axis=1, inplace=True)

# Test set generation is an often neglected but critical part of a machine learning

""" 2. Explore and Visualize the Data to Gain Insights """