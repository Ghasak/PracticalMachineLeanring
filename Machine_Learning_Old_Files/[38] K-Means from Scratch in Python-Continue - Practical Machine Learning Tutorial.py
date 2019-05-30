
"""
Non-supervised machine learning techniques (Flat Clustering)
less No. 37
MacPro
Thu. Aug. 23rd 2018, 15:40:52
Web-link:
https://www.youtube.com/watch?v=H4JSN_99kig&index=37&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&frags=pl%2Cwn
Python version = 4.6
Environment = MacPro_Env
Topic:
Machine Learning - Clustering Introduction
algorithm:
K-Means algorithm (Clustering and Unsupervised machine learning)

We will take some code from the part .34
"""
"""
Non-supervised machine learning techniques
less No. 38
MacPro
Thu. Aug. 23rd 2018, 15:40:52
Web-link:
https://pythonprogramming.net/machine-learning-clustering-introduction-machine-learning-tutorial/
Python version = 4.6
Environment = MacBook_Env
Topic:
Machine Learning -Clustering Introduction
algorithm:
K-Means algorithm (Clustering and Unsupervised machine learning)
Current Update location :~/Volumes/MacPro [Time Machine]/MEGA/MEGAsync/[8] Programming Cloud/[9] Python_codes/Machine_Learning
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

#########################################################
#       Input the dataset (features)
#########################################################

x = np.array([[1,2],
              [1.5,1.8],
              [5,8],
              [8,8],
              [1,0.6],
              [9,11]])



plt.scatter(x[:, 0], x[:, 1], s=150, linewidths=5)
#plt.show()

#########################################################
#       Applying your machine learning tech.
#########################################################

colors = 10*["r", "b", "k", "g", "c"]  # green, red , cyan, blue , black, orange


#########################################################
#       Define our Class of K-Means
#########################################################


class K_Means:
#########################################################

    def __init__(self, k=2, tol=0.001, max_iter=300):
        # K: is the number of classes, tolerance and max number of Iter
        self.k = k
        self.tol = tol
        self.max_iter = max_iter
##########################################################

    def fit(self, data):
        self.centroids = {}
        counter = 1

        for i in range(self.k):
            self.centroids[i] = data[i]             # We will select the first two data set as a centroids

        for i in range (self.max_iter):
            self.classifications = {}               # This will change every time to find the real centroids

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:                 # I have changed X to Data which he forgot to do.
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))        # the minimum distances are the classes
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                # To redefine the new centroid for us then.
                # if you remove this loop you will get the initial centroids (first guess)
                # this here will re-iterate to find the real locations of the centroids of the classes.
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            Optimized = True


            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]

                if np.sum((current_centroid-original_centroid)/original_centroid*100.0) > self.tol:
                    # To show the number of iterations to our classifier we can get
                    Iter = (np.sum((current_centroid-original_centroid)/original_centroid*100.0))
                    print("Number of Iterations is = {} of {}".format(counter, Iter))
                    Optimized = False
                    counter += 1


            if Optimized:
                break
##########################################################

    def predict(self,data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))  # the minimum distances are the classes
        return classification


#########################################################
#       Define our Class of K-Means
#########################################################

clf = K_Means()
clf.fit(x)

for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1],
                marker="o", color="k", s=150, linewidths=5)

for classificiation in clf.classifications:
    color =colors[classificiation]
    for featureset in clf.classifications[classificiation]:
        plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=150, linewidths=5)


# Lets do some prediction here


unkowns = np.array([[1, 3],
                    [8, 9],
                    [0, 3],
                    [5, 4],
                    [6, 4], ])

for unkown in unkowns:
    classificiation = clf.predict(unkown)
    plt.scatter(unkown[0], unkown[1], marker="*", color=colors[classificiation], s=150, linewidths=5)

plt.show()






