
from statistics import mean
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


xs = [1,2,3,4,5,6]
ys = [5,4,6,5,6,7]

# plt.plot(xs,ys)
# plt.show()

# Since above are not np array they are just a python array, to change them which will give us
# more powerful way to iterate over then values in the array,

xs = np.array(xs, dtype = np.float64)  # you can also specify the data-type into your array
ys = np.array(ys, dtype = np.float64)


# first we need a function to calculate the slop as

def best_fit_slop(xs,ys):

    m = ( ((mean(xs)*mean(ys)) - mean(xs*ys)) /
          (mean(xs)**2-mean(xs**2)))

# remember the PEMDAS the order of the operations in computing
    return m

m = best_fit_slop(xs,ys)
print(m)
