# ==================================================================
## {Description} -Mean Shift Intro - Practical Machine Learning Tutorial with Python p.39
# ==================================================================
## {License_info}
# ==================================================================
## Author: {G}
## Copyright: Copyright {year}, {project_name}
## Credits: [{credit_list}]
## License: {license}
## Version: {mayor}.{minor}.{rel}
## Maintainer: {maintainer}
## Email: {contact_email}   
## Status: {dev_status}
# ==================================================================
# Import Libraries
import numpy as np
from sklearn.cluster import MeanShift, KMeans
from sklearn import preprocessing,  model_selection  # before it was cross_validation
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

import xlrd # This one not needed but it is used within the sklearn and pandas.
# -----------------------------------------------------
# Installing packages -
# -----------------------------------------------------
import datetime as dt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd


style.use('ggplot')
'''
Pclass Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
survival Survival (0 = No; 1 = Yes)
name Name
sex Sex
age Age
sibsp Number of Siblings/Spouses Aboard
parch Number of Parents/Children Aboard
ticket Ticket Number
fare Passenger Fare (British pound)
cabin Cabin
embarked Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
boat Lifeboat
body Body Identification Number
home.dest Home/Destination
'''
# https://pythonprogramming.net/static/downloads/machine-learning-data/titanic.xls
# xls = pd.ExcelFile('titanic.xls')

# Prepare a directory file for our current file
import os
import os.path as path
ResourceDir = os.getcwd()
# ---------------------------------------------------
# Create a directory to export data to it.
# if not os.path.exists(ResourceDir+"/resources/stock_dfs/"):
#         os.makedirs(ResourceDir+"/resources/stock_dfs/")
# ---------------------------------------------------

df = pd.read_excel(ResourceDir+'/resources/titanic.xls')

original_df = pd.DataFrame.copy(df)
df.drop(['body','name'], 1, inplace=True)
df.fillna(0,inplace=True)

def handle_non_numerical_data(df):

    # handling non-numerical data: must convert.
    columns = df.columns.values

    for column in tqdm(columns):
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]

        #print(column,df[column].dtype)
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:

            column_contents = df[column].values.tolist()
            #finding just the uniques
            unique_elements = set(column_contents)
            # great, found them.
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    # creating dict that contains new
                    # id per unique string
                    text_digit_vals[unique] = x
                    x+=1
            # now we map the new "id" vlaue
            # to replace the string.
            df[column] = list(map(convert_to_int,df[column]))

    return df

df = handle_non_numerical_data(df)
df.drop(['ticket','home.dest'], 1, inplace=True)

X = np.array(df.drop(['survived'], 1).astype(float))
X = preprocessing.scale(X)
y = np.array(df['survived'])

clf = MeanShift()
clf.fit(X)

# We will add the following to our code
labels = clf.labels_
cluster_centers = clf.cluster_centers_
original_df['cluster_group'] = np.nan

for i in range(len(X)):
    original_df['cluster_group'].iloc[i] = labels[i] # iloc is a reference to the dataframe in pandas refer to the row

n_clusters_ = len(np.unique(labels))

survival_rates = {}
for i in tqdm(range(n_clusters_)):
    temp_df = original_df[(original_df['cluster_group'] == float(i))]
    survival_cluster = temp_df[(temp_df['survived'] == 1)]
    survival_rate = len(survival_cluster)/len(temp_df)
    survival_rates[i] = survival_rate

print(survival_rates)

print(original_df[ (original_df['cluster_group']==1) ])
print(original_df[ (original_df['cluster_group']==0) ].describe())
print(original_df[ (original_df['cluster_group']==2) ].describe())
cluster_0 = (original_df[ (original_df['cluster_group']==0) ])
cluster_0_fc = (cluster_0[ (cluster_0['pclass']==1) ])
print(cluster_0_fc.describe())








