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
# [[plt.scatter(ii[0],ii[1],s = 100, color = i) for ii in dataset[i]] for i in dataset]
# plt.scatter(new_features[0],new_features[1],s =100, color = 'blue')
# plt.show()


# Now we will define our own Ks-neighbor algorithm
# we have to compare a data-point to other data-point, which means we have to do a comparison
# the new data-point to every data point we are having in the original dataset
# we have to grab a list of list of the data-points


def k_nearest_neighbors(data,predict, k =3):                # k means the classifier order, or you can say its the group plus 1 or more


    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups!')  # voting group in our case are k and r which are 2
    # here we will calculate the Euclidean distance
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))  # this one is fast from numpy
            # in the step before, you could have used the following function
            # sqrt( (feature[0]-predict[0])**2  +  (feature[1]-predict[1])**2 )
            # but it has two bad limitations, first its slower than the above
            # its working only for two dimension features (only x1,and x2) but in our model we can use so many features
            # to solve the second issue you could have used the following function
            # np.sqrt( np.sum( (np.array(feature)-np.array(predict))**2 ) )

            distances.append([euclidean_distance,group])
            # you can also do the distance only as:   distance.append(euclidean_distance)
            # the purpose of using the group and making a list in the distance list is to use the sort method
            # which will tell us the group after being sorted and the distances

    votes = [i[1] for i in sorted(distances)[:k]] # sorted is a function to sort an array from smallest to largest
    # this is an equivalent to the following
    # for i in sorted(distances) [:k]:
    #     i[i]
    # i[1] means bring the column no. 1 from the list distance[euclidean_distance,group] which is the group in that case.
    # after sorting we are looking for :k elements only from the smallest to know what group they are holding
    print(Counter(votes).most_common(1))  # this one will print the most common element and how many times it has been mentioned.
    vote_result = Counter(votes).most_common(1)[0][0]   # its a tuple in an array, which back to you the most common
    # [0] means the first element in the tuple, [0] means the first element in the list

    return vote_result

# Lets run our algorithm now and see the results
result = k_nearest_neighbors(dataset,new_features,k = 3)
print(result)


[[plt.scatter(ii[0],ii[1],s = 100, color = i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0],new_features[1],s =100, color = 'blue')
plt.show()
