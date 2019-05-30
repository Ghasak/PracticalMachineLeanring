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
    def __init__(self, visualization = True): # visualization is used with a boolean variable.
        self.visualization = visualization
        self.colors        = {1:'r',-1:'b'}  # Color of the classes, one red for +1 and blue of -1
        if self.visualization:
            self.fig = plt.figure()
            self.ax  = self.fig.add_subplot(1,1,1)  # simply add a subplot as a grid to for the plotting

    # now we will define the method of fitting (notice you can add pass in the end of the method
    # in case you dont know what to add yet,
    # This method (fit) actually is the training of the data
    def fit(self, data):
        pass
    # now we will define a method to make the predication
    def predict(self,features):
        # should return the sign of the class, as sign(x.w+b)
        # you can make a lambda expression for upper than 1 and lower than 1
        # or you can simply use the numpy sign function,
        classification = np.sign(np.dot(np.array(features),self.w)+self.b)
        
        return classification









# now we will start with simple data and later we will extend
data_dict = {-1:np.array([[1,7],
                          [2,8],
                          [3,8],]),
              1:np.array([[5,1],
                          [6,-1],
                          [7,3],])}


