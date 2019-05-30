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




# Simple example on programming the Euclidean distance
point1 = [1,3]
point2 = [2,5]
def euclidean_distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
ed1 = euclidean_distance(point1,point2)
print('euclidean_distance = ', ed1)




