'''
    CHAPTER TWO
        End-to-End Machine Learning Project
        1. Look at the big picture.
        2. Get the data.
        3. Discover and visualize the data to gain insights.
        4. Prepare the data for Machine Learning algorithms.
        5. Select a model and train it.
        6. Fine-tune your model.
        7. Present your solution.
        8. Launch, monitor, and maintain your system.

    - Using ENV00_HANDSON_ML_SCIKITLEARN_KERAS_TENSORFLOW -Environment Python 3.7.x MacPro
'''

# We will use we chose the California Housing Prices dataset from the StatLib repository

'''
        Welcome to Machine Learning Housing Corporation! The first task you are asked to perform is to build a model of housing prices in California using the California cen‐ sus data. This data has metrics such as the population, median income, median housing price, and so on for each block group in California. Block groups are the smallest geographical unit for which the US Census Bureau publishes sample data (a block group typically has a population of 600 to 3,000 people). We will just call them “districts” for short.
        Your model should learn from this data and be able to predict the median housing price in any district, given all the other metrics.
'''

# Step 2

'''
        Okay, with all this information you are now ready to start designing your system. First, you need to frame the problem: is it supervised, unsupervised, or Reinforce‐ ment Learning? Is it a classification task, a regression task, or something else? Should you use batch learning or online learning techniques? Before you read on, pause and try to answer these questions for yourself.
        Have you found the answers? Let’s see: it is clearly a typical supervised learning task since you are given labeled training examples (each instance comes with the expected output, i.e., the district’s median housing price). Moreover, it is also a typical regres‐ sion task, since you are asked to predict a value. More specifically, this is a multiple regression problem since the system will use multiple features to make a prediction (it will use the district’s population, the median income, etc.). It is also a univariate regression problem since we are only trying to predict a single value for each district. If we were trying to predict multiple values per district, it would be a multivariate regression problem. Finally, there is no continuous flow of data coming in the system, there is no particular need to adjust to changing data rapidly, and the data is small enough to fit in memory, so plain batch learning should do just fine.
'''

import os
import tarfile
from six.moves import urllib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from zlib import crc32   # This library to create a hash identifier to not repeat our training set
from sklearn.model_selection import train_test_split

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path = housing_path)
    housing_tgz.close()

import pandas as pd

def load_housing_data(housing_path = HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


def Housing_hist():
    housing.hist(bins=50, figsize=(20,15))
    plt.show()


# Create a Test Set
def split_train_test(data,test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size    = int(len(data) * test_ratio)
    test_indices     = shuffled_indices[:test_set_size]
    train_indices    = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

def ensure_our_dataset_no_repetition(data):
    print("==============================================================================")
    print("======= Adding a Hashing Data to prevent from using same testing set =========")
    print("==============================================================================")
    housing_with_id = data.reset_index() # adds an `index` column
    train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")
    # This is the most stable method with identifer column since we don't have before
    housing_with_id["id"] = data["longitude"] * 1000 + data["latitude"]
    train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")
    print("Original Data set")
    print(housing_with_id)
    print("Training set")
    print(train_set)
    print("Testing set")
    print(test_set)


def spliting_another_method_from_sklearn(data):
    print("==============================================================================")
    print("================ SPLITING USING SKLEARN LIBRARY ==============================")
    print("==============================================================================")
    # Here you will need sklearn.model_selection
    train_set, test_set = train_test_split(data, test_size = 0.2, random_state = 42)
    print("Original Data set")
    print(data)
    print("Training set")
    print(train_set)
    print("Testing set")
    print(test_set)

if __name__ == "__main__":
    fetch_housing_data()
    housing = load_housing_data()
    #print(housing.head())
    #print(housing.info())
    #print(housing['ocean_proximity'].value_counts())
    #Housing_hist()
    train_set, test_set = split_train_test(housing, 0.2)
    print(f"The size of training set is = {len(train_set)} and the size of test set is = {len(test_set)}")
    #ensure_our_dataset_no_repetition(housing)
    spliting_another_method_from_sklearn(housing)
    # 56 | Chapter 2: End-to-End Machine Learning Project
