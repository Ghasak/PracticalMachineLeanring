# We will learn how to write our own code for the Ks-neighbor algorithm
# starting with an introduction on the Euclidean distance
"""
Define:
Euclidean Distance - Practical Machine Learning

"""
from math import sqrt
import numpy as np
import warnings                     # to warn the user when they using a wrong number for k
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
from collections import Counter     # to create the vote basically


# First to make the dataset using dictionary
dataset = {'k': [[1,2], [2,3], [3,1]], 'r': [[6,5], [7,7], [8,6]]}

new_features = [5,7]  # from first guess, it seems this value belongs to the class r more
#
# for i in dataset:                   # for each key in the dictionary which are 1,2
#     for ii in dataset[i]:           # for each feature set which means for k it would be 1,2,3
#         plt.scatter(ii[0],ii[1], s=100, color = i)    # here you are reading the list of feature 1 which are only two elements 1,2
#
# you can achieve the above similarly by introduce the power of python programming language
[[plt.scatter(ii[0],ii[1],s = 100, color = i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0],new_features[1],s =100, color = 'blue')
plt.show()


# Now we will define our own Ks-neighbor algorithm

def k_nearest_neighbors(data,predict, k =3):                # k means the classifier order, or you can say its the group plus 1 or more


    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups!')  # voting group in our case are k and r which are 2

    # knnalogs
    return vote_result



