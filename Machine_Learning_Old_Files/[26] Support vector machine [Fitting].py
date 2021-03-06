# Here we will use the support vector machine
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


# Lets try to write the basic of support vector machine
# we will use a class of several objects and methods

class Support_Vector_Machine:
    # when you call a class to run, none of the methods will run except the __init__ one
    def __init__(self, visualization=True):  # visualization is used with a boolean variable.
        self.visualization = visualization
        self.colors = {1: 'r', -1: 'b'}  # Color of the classes, one red for +1 and blue of -1
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1, 1, 1)  # simply add a subplot as a grid to for the plotting

    # now we will define the method of fitting (notice you can add pass in the end of the method
    # in case you don't know what to add yet,
    # This method (fit) actually is the training of the data
    def fit(self, data):
        self.data = data
        # here we will create a dictionary with ||w||:[w,b] see the theory to understand more
        # first we will create an empty dictionary and later we will populate it with these information
        opt_dict  = {}

        # as we learn before this is the transforms to check read the theory
        # each time a vector is created we check with the transform here
        transforms = [[1,1],
                      [-1,1],
                      [-1,-1],
                      [1,-1]]
        # lets check the maximum and minimum range of the data
        all_data = []
        # yi is the class name which is the output,
        # yi is -1 or +1
        for yi in self.data:                    # to iterate through classes
            for featureset in self.data[yi]:    # to iterate through features for e.g. [1,7] is 1 then [2,8] is 2
                for feature in featureset:      # to iterate through points 1,7
                    all_data.append(feature)    # to append them to a list populated with the numbers

        # Now we can use the max function to know largest value in our data
        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        # now since you got these values they will be stored and you can now get ride of matrix
        all_data = None


        # Now recall the picture of the big U shape, first we take a large steps and the medium and later small once we
        # reach to the optimum value we want
        # we can also thread or multi-processed
        step_size = [self.max_feature_value * 0.1,       # Big Step
                     self.max_feature_value * 0.01,       # Medium Steps
                     self.max_feature_value * 0.001]       # Small (expensive) steps

        b_range_multiple = 5    # extremely expensive,  we dont care about b that much

        #
        b_multiple =5

        latest_optimum =self.max_feature_value*10       # this the largest vector w will be equal to this number


        # Now we will start the stepping

        for step in step_size:
            w = np.array([latest_optimum,latest_optimum])
            # we can do this because convex
            optimized = False  # until we run out of our step_size
            while not optimized:
                pass
            












    # now we will define a method to make the predication
    def predict(self, features):
        # should return the sign of the class, as sign(x.w+b)
        # you can make a lambda expression for upper than 1 and lower than 1
        # or you can simply use the numpy sign function,
        classification = np.sign(np.dot(np.array(features), self.w) + self.b)

        return classification


# now we will start with simple data and later we will extend
data_dict = {-1: np.array([[1, 7],
                           [2, 8],
                           [3, 8], ]),
             1: np.array([[5, 1],
                          [6, -1],
                          [7, 3], ])}


