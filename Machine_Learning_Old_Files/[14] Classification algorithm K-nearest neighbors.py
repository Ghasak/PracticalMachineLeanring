# Here we will learn about the classification algorithm starting with
# K-nearest neighbour

"""
Definition:
We are going to use the breast cancer Wisconsin (original) dataset
go to the attribute part in the meta data to understand what all the variables are about
we want to classify the tumor type to
                            2 : benign
                            4 : malignant

There are 16 instances in Groups 1 to 6 that contain a single missing  (i.e., unavailable) attribute value, now denoted
by "?"
Class distribution:
                            Benign    : 458 ( 65.5 %)
                            Malignant : 241 ( 34.5 %)
"""

import numpy as np
from sklearn import preprocessing, model_selection, neighbors    # remember model_selection is not instead cross_validation
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.txt')
# you could have name the columns as we did before in the linear regression but we simply named them in the sublime text
df.replace('?', -99999, inplace= True)  # we will remove the missing values and assign -99999 to them
# we can remove the id since it has no impact on the features and the model fitting
df.drop(['id'], 1, inplace= True)  # maybe here without the brackets also ok


X = np.array(df.drop(['class'],1))
y = np.array(df['class'])

# here we will do the split the data and shuffle the data

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y, test_size = 0.2)

# Here we will define our classifier and apply the fitting the data set,

clf = neighbors.KNeighborsClassifier()  # making an object from the KNeighborsClassifier class
clf.fit(X_train,y_train)

# or simply you can say    neighbours.KNeighborsClassifier.fit(...etc

accuracy = clf.score(X_test, y_test)
print(accuracy)


# Here we will make a prediction for our dataset
example_measures = np. array([4,2,1,1,1,2,3,2,1])  # we are adding here a one case of patient and try to see
# the value of this patient is not existed in the data and its unique and never seen before by the model
example_measures = example_measures.reshape(1,-1)  # here we are making the example_measures as a vector (list) using the
# reshape method which is simply needs the No.rows and No.column, and if you use -1 it will be only one line (row)
prediction = clf.predict(example_measures)
print(prediction)

# lets test the results even further by adding two more more patients

example_measures_2 = np. array([[4,2,1,1,1,2,3,2,1],[4,2,2,2,2,2,3,2,1],[8,10,10,8,7,10,9,7,1]])
example_measures_2 = example_measures_2.reshape(len(example_measures_2),-1)
prediction2 = clf.predict(example_measures_2)
print(prediction2)









