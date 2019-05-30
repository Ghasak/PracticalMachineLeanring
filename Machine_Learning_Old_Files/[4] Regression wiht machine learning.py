import math
import pandas as pd
import quandl
import numpy as np    # this will help use to define array which python doesnt have such feature, for doing math
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

"""
1. preprocessing: this gives us quite a few things, but we're actually going to be using the scaling 
scaling your daa aspect is usually done {on} the features (X) and the goal is often to get your features to be between
somewhere between negative 1 and a positive 1 this can just help with accuracy as well as just processing speed or how long
it might take to actually do the calculations
2. model_selection (before it was cross_validation): We're going to use cross-validation to create training and testing samples. 
It's just a really nice way
to split up your data, to not have a biased data
3. svm: this is a support vector machine learning package, at least for now we are not going to use it, just the 
leaning regression only here, from the svm

"""


df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT']     = (df['Adj. High']-df['Adj. Close']) / df['Adj. Close'] *100
df['PCT_change'] = (df['Adj. Close']-df['Adj. Open']) / df['Adj. Open']  *100

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
forecast_col = 'Adj. Close'
df.fillna(-99999,inplace =True)
forecast_out = int(math.ceil(0.01*len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

df.dropna (inplace = True)

#print(df.head)
# so far the df is the data-frame that we are working on not lets split both the features X and the label y
#feature is x and labels will be y
X = np.array(df.drop(['label'],1))
y = np.array(df['label'])

X = preprocessing.scale(X)
# X = X[:-forecast_out+1]
# df. dropna(inplace=True)
y = np.array(df['label'])

print(len(X),len(y)) # checking the lenght of both array and I found they are matching to 3389 cases

# the training part is here

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2)
# shafeling the data here and output for 20% for test and 80% for training the model

# here we will do the classifier fit
clf = LinearRegression() # make an object from this class, called clf, which we can now access all
# the methods (functions) in it

clf.fit(X_train,y_train)  # this is for train the data

accuracy = clf.score(X_test,y_test)  # this is for testing the data and assign it to accuracy (or you can call it
# confidence, here the accuracy is actually the square error R2

# lets test our fitting now,
print(forecast_out)  # we are predicating 30 days in advance
print("The results of linearRegression from model_selection module is ....................=",accuracy)


# if you need to use another algorithm to fit you data you can here use svm as following
clf_support_vector = svm.SVR()
clf_support_vector.fit(X_train,y_train)
accuracy2 = clf_support_vector.score(X_test,y_test)
print("The results of linearRegression from support vector svm module is .................=",accuracy2)


# you can change the kernel function in the Support vector regression algorithm as

clf_support_vector_2 = svm.SVR(kernel = 'poly')
clf_support_vector_2.fit(X_train,y_train)
accuracy3 = clf_support_vector_2.score(X_test,y_test)
print("The results of linearRegression from support vector svm with poly kernel module is =",accuracy3)



