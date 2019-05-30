# lets try to understand some tricks and tips for python
import numpy as np
# now we will start with simple data and later we will extend
data_dict = {-1: np.array([[1, 7],
                           [2, 8],
                           [3, 8], ]),
             1: np.array([[5, 1],
                          [6, -1],
                          [7, 3], ])}

all_data = []
# yi is the class name which is the output,
# yi is -1 or +1
for yi in data_dict:  # to iterate through classes
    for featureset in data_dict[yi]:  # to iterate through features for e.g. [1,7] is 1 then [2,8] is 2
        for feature in featureset:  # to iterate through points 1,7
            all_data.append(feature)

print (all_data)
print(max(all_data))


# Now we can use the max function to know largest value in our data
max_feature_value = max(all_data)
min_feature_value = min(all_data)
# now since you got these values they will be stored and you can now get ride of matrix
all_data = None



# from Class P.[27] video we will add the following
transforms = [[1, 1],
              [-1, 1],
              [-1, -1],
              [1, -1]]

step_size = [max_feature_value * 0.1,  # Big Step
                     max_feature_value * 0.01,  # Medium Steps
                     max_feature_value * 0.001]  # Small (expensive) steps

b_range_multiple = 5  # extremely expensive,  we don't care about b that much

# we dont need to take as small steps with b as we do with w
b_multiple = 5

latest_optimum = max_feature_value * 10  # this the largest vector w will be equal to this number

# Now we will start the stepping

for step in step_size:
    w = np.array([latest_optimum, latest_optimum])
    # we can do this because convex
    optimized = False  # until we run out of our step_size
    while not optimized:
        for b in np.arange(-1*(max_feature_value*b_range_multiple),   # range from
                               max_feature_value*b_range_multiple,
                               step*b_multiple):
            for transformation in transforms:
                w_t = w*transformation


print(w_t)