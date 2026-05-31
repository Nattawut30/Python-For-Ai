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

# Download and prepare the data
data_root = "https://github.com/ageron/data/raw/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# Visualize the data
lifesat.plot(kind='scatter', grid=True,
             x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

# Select a linear model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Make a prediction for Cyprus
X_new = [[37_655.2]] # Cyprus' GDP per capita in 2020
print(model.predict(X_new)) # [[6.30165767]]

# ==============================

# 1.2: Training and running a k-nearest neightbors regression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

# Download and prepare the data
data_root = "https://github.com/ageron/data/raw/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# Visualize the data
lifesat.plot(kind='scatter', grid=True,
             x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

# Select a linear model
model = KNeighborsRegressor(n_neighbors=3)

# Train the model
model.fit(X, y)

# Make a prediction for Cyprus
X_new = [[37_655.2]] # Cyprus' GDP per capita in 2020
print(model.predict(X_new)) # [[6.3333333]]

# Studied the data
# Selected a model
# Trained it on the training data
# Applied the model to make prediction on new cases

""" 3. Main Challenges of ML """

# Insufficient Quantiity of Training Data
# - It takes a lot of data for most machine learning algorithm to work properly
# - Data matters more than algorithms, but don't abandon algorithms yet

# Non-representative training data
# - To generalize well, the training data must be representative of the new cases you want to generalize to

# Poor Quality Data
# - Data is full of errors, outliers and noise = make it harder for the system to detect the underlying pattern
# - You will spend 80% of your time clean traning data
# - Decide it on you want to ignore the attibutes altogether or not. Keep it or remove it or combine it

# Irrelevant Features
# - Garbage in, Garbage out = the training data contains enough relevant features = good
# - Feature Selection: selecting the most useful features
# - Feature Extraction: combining existing features to produce a more useful one
# - New Features: gathering new data

# Overfitting the Training Data
# - the model perform well on the training data, but it does not generalize well
# - happends when the model is too complex relative to the amount and noisiness of the training data
# - Solutions: Simplify the model, Gather more data, Reduce the noise 

# Regularization: Constraining a model to make it simpler and reduce the risk of overfitting
# Hyperparameter: A parameter of a learning algorithms. Tuning hyperparameters is an important part of ML

# Underfitting the Training Data
# - Opposite of overfitting: it occur when the model is simple to learn the underlying structure of the data
# - Solutions: Select a more powerful model, Feed better features to the algorithm, Reduce the constraints on the model

""" 4. Testing and Validating """
# Try it out one new case
# - Deployed in a production and monitoring
# - To split the data into 2 sets: the training set and the test set.

# Evaluating the model on the test set, get an estimate of the error.
# This value tells you how well the model will perform on instances it has never seen before

# Hyperparameter Tuning and Model Selection
# - To train both and compare how well they generalize using the test set
# - You train multiple models with various hyperparameters on the reduced training set
# - You select the model that perform best on the validation set
# - You evaluate this final model on the test set to get an estimate of the generalization error

# It is not ideal to compare candidate models trained on a much smaller training set
# Solutions: To perform repeated cross-validation or using small validation sets

# Data Mismatching
# - Both validation set and the test set must be as representative as possible of the data you expect to use in production
# - Making sure that no duplicates or near-duplicates end up in both sets
# - If it performs well on the train-dev set, then you can evaluate the model on the dev set.
# - If it performs bad, then the problem must be coming from the data mismatch

# Once you have a model that performs well on both the train-dev set and the dev set,
# You can evaluate it one last time on the test set to know how well it is likely to perfrom in productions.

# No Free Lunch (NFL): If you make absolutely no assumption about the data, then there's no reason to prefer one model over any other!