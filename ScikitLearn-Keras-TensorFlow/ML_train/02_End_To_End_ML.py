""" Chapter 02: End-To-End Machine Learning Project """

# Imagine you are a data scientist at a real-estate company
# California housing prices datasets
# The model should learn from the data and be able to predict the median housing price in any district

""" 1. Frame the problem """

# - The first question to ask your boss is what exactly the business objective
# - Knowing the objective: How you frame the problem, which algorithms you will use, which performance to measure
# - The next questions to ask your boss is what the current solution looks like

# Pipeline
# - A sequence of data processing components
# - Commonly use it in ML systems because a lot of data to manipulate and data transformations.
# - Each component pulls in a large amount of data, processes it, and spits out the result in data store.
# - The next component in the pipeline pulls in this data and spits out its own output.
# - Different teams can focus on different component.
# - A broken component can go unnoticed for some time if proper monitoring is not implemented.

# Fist, Determine what kind of training supervision the model will need?
# If the data were hugh, you could either split your batch learning work across multiple servers

""" 2. Select a Performance Measure """

# - A typical performance measure for regression problems is the "root mean square error (RMSE)"

# RMSE(X, h) = sqrt[1/m Σm, i=1 (h(x^i) - y^i)^2)]

# - It gives an idea of how much error the system typically makes in its predictions,
# - With a higher weight given to large errors 

# Notations
# - m is the number of instances in the dataset you are meansuring the RMSE on.
# - x^(i) is a vector of all the feature values (excluding the label) of the i^th instance in
#   the datasets and y^(i) is its label (the desired output value for that instance).
# - X is a matrix containing all the feature values (excluding labels) of all instances in the dataset.
#   There is one row per instance, and the i^th row is equal to the transpose of x^(i), noted (x^(i))^t.
# - h is your system's prediction function, also called a hypothesis.
# - RMSE(X, H): is the cost function measured on the set of examples using hypothesis h

# If there are many outlier. districts. In that case, you may consider using the "mean absolute error"
# MAE also called the average absolute deviation

# MAE(X, h) = 1/m Σm, i=1|h(x^i) - y^i|

# Both RMSE & MAE use to measure the distance between 2 vectors
# - the vector of predictions
# - the vector of target values

# - Computing the root of a sum of sqares (RMSE) corresponds to the "Euclidean norms"
# - Computing the sum of absolutes (MAE) corresponds to norm is "Manhattan norm" (measure the distance between 2 points)
# - Gives the number of non-zero elements in the vector, and the maximum absolute value in the vector.

# The higher the norm index, the more it focuses on large values and neglects small ones.
# This is why the RMSE is more sensitive to outliers than the MAE.
# But if it's a bell-shpaed curve, the RMSE performs well and preferred.

""" 3. Check the Assumptions """

# Verify the assumptions that have been made so far;
# This can help you catch a serious issues early on

# verifing the objective and expectations clearly before doing the work

# Get the data and work on it

""" 4. Get the Data """

# Jupyter Notebook = interactive documents containing text, images, and executable code snippets (Python)
# Run it on Google Colab or Extension on IDE
# .ipynb

# A jupyter notebook is composed of a list of cells. Each cell contains either executable code or text
# press shift + enter to run
# the code runs on the runtime, not on your machine

# if you runs it on IDE likes VScode with the jupyter extension, the runtimes will be in "kernel"
# Don't forget to save a copy of your code

# You can mount the google drive on the runtime allowing the notebook to read and write files directly to Google Drive as if it were local directory

""" 5. The power and Danger of Interactivity """

# Jupyter Notebook are interactive
# It's very easy to run cells in the wrong order, or to forget to run a cell

# If you encounter the weird error, trt restarting the runtime
# Or adjust the kernel

""" 6. Download The Data """
# You will need a single compressed file which contains a comma-separated-values or "CSV"

# 2.1: Fetching and loading the data
from pathlib import Path
import pandas as pd
import tarfile
import urllib.request

def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

housing = load_housing_data

""" 7. Quick look at the data """

# Use "housing.head()"" function = Top five rows in the datasets
# Use "housing.info()" function = get a quick description of the data in particular total number of rows

# >>> housing["ocean_proximity"].value_counts()

# Use "housing.describe() function = Shows a summary of the numerical attributes"
# The count, mean, min, max rows are self explanatory. The null values are ignored
# The std rows show "standard deviation" measures how dispersed the values are
# 25%, 50%, 75%, rows show the "percentile"

# hist() plot a histogram for each numerical attribute
import matplotlib.pyplot as plt

housing.hist(bins=50, figsize=(12, 8))
plt.show()

# Working with preprocessed attributes is common in ML
# The latter may be a serious problem since it is your target attribute (your labels)
# 1. collect proper labels for the deistricts whose labels were capped
# 2. Remove those districs from the training set

# Many histograms are skewed right, they extend much farther to the right of the median than to the left. make it hard for ML to see patterns.

# *** Create a test set, put it aside, and never look at it. ***
