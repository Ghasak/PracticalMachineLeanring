# here we will learn to use the machine learning with the stock prices to learn and fitting the data.
# features and attributes, features are x and attributes are y's
import math
import pandas as pd
import quandl

# you can visit https://www.quandl.com/tools/python
# to get the data that you need, https://www.quandl.com/search?query=googl%20stock
# the data with wiki dataset, which is a simple dataset.for free only 50 calls a day you r permited
# I have fixed an error in quandl, which is change form Quandl to quandl
df = quandl.get('WIKI/GOOGL')


df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High']-df['Adj. Close']) / df['Adj. Close'] *100 # we are defining a new variable
# here from the date-frame we defined earlier
df['PCT_change'] = (df['Adj. Close']-df['Adj. Open']) / df['Adj. Open'] *100

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']] # Our new data clearned and ready to input in the leanring


forecast_col = 'Adj. Close'  # this is the outcome that you want to get, which is the Y
df.fillna(-99999,inplace =True) # to replce the missing values in the dataframe, with Panda
# usually the missing values are replaced with 'na' but it will cause a problem for fitting
#forecast_out = int(math.ceil(0.11*len(df)))  # this is before
forecast_out = int(math.ceil(0.01*len(df)))  # this one to make sure the lenght of the dataset multiply by 10%
# of the outcome will make us sure to ceiling the number to higher intger and int to make it very sure its integer,
# maybe this point is not necessary.

df['lable'] = df[forecast_col].shift(-forecast_out)
# print(df[forecast_col].head)
# print(df['lable'].head)

# this step is to make a predication in the future, by shifting the lable 10 days into the future
# thus we used 0.1 of the total days in the future.

df.dropna (inplace = True)
print(df.tail())

# due to large numbers here please change the 0.1 up to 0.01
