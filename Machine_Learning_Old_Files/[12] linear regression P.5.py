
from statistics import mean
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import style
import random   # to make our data random

style.use('fivethirtyeight')

# xs = [1,2,3,4,5,6]
# ys = [5,4,6,5,6,7]

# plt.plot(xs,ys)
# plt.show()

# Since above are not np array they are just a python array, to change them which will give us
# more powerful way to iterate over then values in the array,

# xs = np.array(xs, dtype = np.float64)  # you can also specify the data-type into your array
# ys = np.array(ys, dtype = np.float64)



# Here we will add our dataset random generation for testing our model
def create_dataset(hm, variance, step = 2, correaltion = False):

    """
    Definition:
    hm          : number of data points that you want to create
    variance    : is how variables or scattered your data are
    step        : how far from the average of our data we want to be, default is (2)
    correlation : to show the data r correlated positively or negatively or none (boolean), default (False)
    this function will return a two lists one for xs and one for ys, you can set your variables in that case to the
    form like
    x1, y2 = create_dataset....etc

    """
    val =1 # this would be the first value in the ys
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance,variance) # return a value between these two numbers (-variance,variance)
        ys.append(y)  # this is the way to add value to your list above, I thought before ys[i] = y (which is wrong)
        if correaltion and correaltion == 'pos':
            val += step
        elif correaltion and correaltion == 'neg':
            val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype = np.float64), np.array(ys, dtype=np.float64)

# first we need a function to calculate the slop as

def best_fit_slop_and_intercept(xs,ys):

    m = ( ((mean(xs)*mean(ys)) - mean(xs*ys)) /
          (mean(xs)**2-mean(xs**2)))
    b = mean(ys)-m*mean(xs)

# remember the PEMDAS the order of the operations in computing
    return m,b

def squared_error(ys_orig, ys_line):
    return sum((ys_line-ys_orig)**2)

def coefficient_of_determination(ys_orig,ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]    # to make a vector with only one value which is mean(ys_orig)
    squared_error_regr = squared_error(ys_orig,ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1- (squared_error_regr / squared_error_y_mean)


# create data from the random generation data that we               created
xs, ys = create_dataset(2000, 1700,2,'neg')




m,b = best_fit_slop_and_intercept(xs,ys)
print(m,b)


regression_line = [(m*x)+b for x in xs]
print(regression_line)


# Here we will add the piece of code to calculate the coefficient of determination,
r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)



# this is exact identical to the following format
# for x in xs:
#     regression_line.append((m*x)+b)

# now we will plot the data and the regression line

# what if you want to predict a specific value
predict_x = 8
predict_y = (m*predict_x)+b

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y, s = 100, color = 'red')
plt.plot(xs,regression_line)
plt.show()

