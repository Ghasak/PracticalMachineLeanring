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

DOWNLOAD_ROOT = 'http://raw.githubusercontent.com/ageron/handson-m12/master/'
HOUSING_PATH  = os.path.join("datasets","housing")
HOUSING_URL   = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

