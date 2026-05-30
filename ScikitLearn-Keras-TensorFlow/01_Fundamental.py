""" Chapter 1: The machine learning landscape """

# The first ML in the world = Spam folders
# What is machine learning? = The field of study that gives computers the ability to learn without being explicity programmed

# Trainning set = the examples that the system uses to learn
# Training instance or sample = each traning example
# Model = the part of a machine larning system that learns and makes predictions

# Why use them?
# 1. Test the program and repeat steps 1-2 untill it was good to launch
# 2. Detecting unusually frequent patterns of activities
# 3. When encounters a way too complex for traditional approaches or have no know algorithm

# Supervised Learning
# : the trainnig set you feed to the algorithm includes the desired solutions
# : A typical supervised learning task is classification, spam folders filters 
# : Another typical task is to predict a target numeric value, price of a car, given a set of features (age, brand)
# : Logistic Regression

# Unsupervised Learning
# : The traning data is unlabeled
# : The system learn without a teacher
# : Clustering, Hierarchical Clustering, Visualization Algorithm
# : dimensionality reduction = simplify the data without losing too much information, merge several correlated features into one

# * Better reduce thenumber of dimensions in your traning data using a dimensionality reduction algorithm
#  before you feed it to another ML algorithm. It runs faster and perform better. *

# Anomaly Detection: detecting unustall credit card transactions to prevent fraud
# Novelty Detection: it aims to detect new instances that look different from all instances in the training set
# Association Rule Learning: dig into learge amounts of data and discover interesting relations between attributes

# Semi-Supervised Learning
# : deal with data that's partially labeled
# : Google Photos combining both supervised and unsupervised

# Self-Supervised Learning
# : Once th whole dataset is labeled, any supervised learning algorithm can be used
# : Tweak & Fine-tune the model for slightly different task
# : Transfer learning = Transferring knowledge from one task to another
# : uses labels during traning, it's closer to supervised learning

# Reinforcement Learning
# : Agent = The learning systems
# : Agent can obserbe the environment select and perform actions get rewards in return or penalties
# : Policy = It must learn by itself what is the best strategy
# : Policy defines what action the agent should do in a given situations
# : DeepMind's AlphaGo program robots implements is a good examples

""" 1. Batch and Offline Learning """

# Batch Learning = it must be tranined using all the available data
# Trained > Launched > Runs without learning anymore = offline learning
# The world changing -> but the model remains the same = model rot / data drift
# Batch learnign system = update the data and train a new version of the system from scratch as often as needed
# If the system need to rapidly adapt such as predict stock price, then we needd a more reactive solution
# Just use algorithms that are capable of learing incrementally

# Online Learning = train the system incrementally by feeding it data instances sequentially
# each learning step is fast and cheap so the system can learn about a new data on the fly as it arrives
# Trained > Launched into production > keep it learning as new data comes in
# Use it to handle huge datasets

# High learning rate => repidly adapt to new data but qucikly forget the old data
# Low learning rate => learn slowly but less sensitive to noise in the new data and sequences data points

# Bad data is fed to the system -> the performance will decline and quickly
# Monitoring the system closely and promptly switch learning off
# Monitoring the input data and react to abnormal data

""" 2. Instance-Based / Model-Based Learning """

# Instance-Based Learnign = Learns the examples, then generalizes to new cases by using a similarity measure to comepre them and learned examples
# Model-Based Learning = build a model of these examples and then use the model to make predictions
# A model selection = noisy data but there're a pattern. decide it as a linear function

# Utility function = meansure how good your model
# Cost Function = how bad it is

# Train the model = runnign an algorithm to find the model parameters that make it best fit the training data

# 1.1: Training and running a linear model using Scikit-Learn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

