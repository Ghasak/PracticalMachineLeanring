import math, datetime
import pandas as pd
import quandl
import numpy as np    # this will help use to define array which python doesnt have such feature, for doing math
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pickle    # to save the model and to not do the training again

from matplotlib import style
style.use('ggplot')

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



#print(df.head)
# so far the df is the data-frame that we are working on not lets split both the features X and the label y
#feature is x and labels will be y
X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out:]
df.dropna (inplace = True)
# X = X[:-forecast_out+1]
# df. dropna(inplace=True)
y = np.array(df['label'])

print(len(X),len(y)) # checking the length of both array and I found they are matching to 3389 cases

# the training part is here

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2)
# shafeling the data here and output for 20% for test and 80% for training the model

# here we will do the classifier fit
# clf = LinearRegression(n_jobs=-1) # make an object from this class, called clf, which we can now access all
# # the methods (functions) in it
#
# clf.fit(X_train,y_train)  # this is for train the data
# # use pickle to save the steps above using the following idea
# with open('linearregression.pickle','wb') as f:
#     pickle.dump(clf,f) # dump the classifier clf into the file f which has the name linearregression.pickle

# to use the classifier from the pickle that we saved above you can use the following

pickle_in = open('linearregression.pickle','rb')
clf=pickle.load(pickle_in)

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



# To Predict the outcome

forecast_set = clf.predict(X_lately)
print(forecast_set,accuracy,forecast_out)  # next 30 days, of stocks prices outcome predication


# Plotting the prediction
df['Forecast'] = np.nan
last_date      = df.iloc[-1].name
last_unix      = last_date.timestamp()
one_day        = 86400
next_unix      = last_unix + one_day


for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

    # to read this last loop its np.nan which is the array that is empty now, to be filled by
    # for _ something we don't care about, by the columns-1 and add the [forcast value i]

# To check what happened previously, we have used two things
# one when there is value of forecast in then end, and when we don't have values,
# to complete the dataframe actually, this steps above were important
print(df.head())
print(df.tail())



df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.show()



# Example to plot the sin wave, not related to the above question
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)
plt.plot(t, s)

plt.grid(True)
plt.show()