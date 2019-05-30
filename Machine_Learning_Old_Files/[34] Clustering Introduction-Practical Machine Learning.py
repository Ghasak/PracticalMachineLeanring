
"""
Non-supervised machine learning techniques
less No. 34
MacBook Pro 13''
Tue Aug 21st 2018, 1:08:21 am
Web-link:
https://pythonprogramming.net/machine-learning-clustering-introduction-machine-learning-tutorial/
Python version = 4.6
Environment = MacBook_Env
Topic:
Machine Learning - Clustering Introduction
algorithm:
K-Means algorithm (Clustering and Unsupervised machine learning)
"""
#########################################################
#       Import the packages (modules)
#########################################################

import matplotlib
matplotlib.use('TkAgg')
# These two commands up you can remove when you use Windows (they are for Mac user)
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans

#########################################################
#       Input the dataset (features)
#########################################################

x = np.array ([[1,2],
              [1.5,1.8],
              [5,8],
              [8,8],
              [1,0.6],
              [9,11]])

#plt.scatter(x[:,0],x[:,1], s = 150, linewidths= 5)
#plt.show()

#########################################################
#       Applying your machine learning tech.
#########################################################

clf = KMeans(n_clusters= 3)   # Changing the n_clusters parameters depending on the
                              # number of classes that you want to separate your data
clf.fit(x)

centroids = clf.cluster_centers_    # to get the centers of the groups
labels    = clf.labels_             # To get the labels of these groups

# print (labels)
colors = 10*[ "r.", "b.", "k.","g.","c."]  # green, red , cyan, blue , black, orange
# 10 has no meaning except its
# expand our choices of selecting color from the list.
# print(colors)
for point in range(len(x)):  # I added point instead of i to show it more clearly.
    plt.plot(x[point][0],x[point][1], colors[labels[point]], markersize = 25)


plt. scatter(centroids[:,0],centroids[:,1], marker = 'x', s = 150 , linewidths= 5)

#########################################################
#       I have added this to put something on terminal
#########################################################

for point in range (len(x)):
    print("The value of x{},y{} =({},{})".format(point,point,x[point][0],x[point][1]) )

print ("####################################################")
print ("##        And the location of the Centers          #")
print ("####################################################")
for point in range (len(centroids)):
    print("Group center No.{} = ({},{})".format(point,centroids[point,0],centroids[point,1]))

plt.show()