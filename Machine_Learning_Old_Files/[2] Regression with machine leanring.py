# here we will learn to use the machine learning with the stock prices to learn and fitting the data.
# features and attributes, features are x and attributes are y's

import pandas as pd
import quandl

# you can visit https://www.quandl.com/tools/python
# to get the data that you need, https://www.quandl.com/search?query=googl%20stock
# the data with wiki dataset, which is a simple dataset.for free only 50 calls a day you r permited
# I have fixed an error in quandl, which is change form Quandl to quandl
df = quandl.get('WIKI/GOOGL')
print(df.head)  # just to see you data first,

print(df.tail())  # to see the data more nicely,

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High']-df['Adj. Close']) / df['Adj. Close'] *100 # we are defining a new variable
# here from the dateframe we defined earlier
df['PCT_change'] = (df['Adj. Close']-df['Adj. Open']) / df['Adj. Open'] *100

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
print(df.tail())

print(df.head())
