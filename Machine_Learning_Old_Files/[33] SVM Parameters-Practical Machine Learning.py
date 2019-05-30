
""""
From the Class of [14] we continue here
Using the MacPro 2018/08/20 19:01
MacPro_Env
Python Version 4.6
Website link:
https://pythonprogramming.net/support-vector-machine-parameters-machine-learning-tutorial/
Fixes applied:
python3 -m pip install --no-binary pandas -I pandas

the Support vector machine website for the package
http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html

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
from sklearn import preprocessing, model_selection, neighbors
# remember model_selection is not instead cross_validation
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

print("The accuracy of fitting is = {}".format(accuracy))