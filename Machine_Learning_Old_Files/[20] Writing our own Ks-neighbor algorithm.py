# We will learn how to write our own code for the Ks-neighbor algorithm
# since there are so many features here we will not plot anything here,
from math import sqrt
import numpy as np
import warnings                     # to warn the user when they using a wrong number for k
from collections import Counter     # to create the vote basically
import pandas as pd                 # to import the dataset from our previous tutorial
import random                       # to shuffle the data


accuracies = []
no_of_checking = 5
for i in range(no_of_checking):
    ####################################
    #  K nearest neighbors algorithm   #
    ####################################
    def k_nearest_neighbors(data,predict, k =3):
        # k means the classifier order, or you can say its
        # the group plus 1 or more

        if len(data) >= k:
            warnings.warn('K is set to a value less than total voting groups!')
            # voting group in our case are
            # k and r which are 2
        # here we will calculate the Euclidean distance
        distances = []
        for group in data:
            for features in data[group]:
                euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))  # this one is fast from numpy
                distances.append([euclidean_distance,group])

        votes = [i[1] for i in sorted(distances)[:k]]
        #print(Counter(votes).most_common(1))
        #  this one will print the most common element and how many times it has been mentioned.
        vote_result = Counter(votes).most_common(1)[0][0]
        confidence  = Counter(votes).most_common(1)[0][1] / k
        # its a tuple in an array, which back to you the most common
        return vote_result, confidence
    # Lets run our algorithm now and see the results
    # result = k_nearest_neighbors(dataset,new_features,k = 3)
    # print(result)
    #
    #
    # [[plt.scatter(ii[0],ii[1],s = 100, color = i) for ii in dataset[i]] for i in dataset]
    # plt.scatter(new_features[0],new_features[1],s =100, color = 'blue')
    # plt.show()

    ################################
    #       Import the data set    #
    ################################
    df = pd.read_csv('breast-cancer-wisconsin.txt')
    df.replace('?',-99999, inplace=True)
    df.drop(['id'], 1,inplace=True)
    # print(df.head)
    full_data = df.astype(float).values.tolist()   # you can change the data-frame to either float or int
    # to ensure some times after you have done the replacement
    # with the ?, it shows some of the values are text like '1'
    # this will help use to overcome this situation
    # print(full_data)   # to check if the data is already imported


    ################################
    #     Shuffle and split data   #
    ################################
    #print(full_data[:5])
    random.shuffle(full_data)
    #print(20*'#')
    #print(full_data[:5])

    ################################
    #     Slice the dataset        #
    ################################

    test_size    = 0.2            # 20% of the data will be used to train the classifier
    train_set    = {2:[] ,4:[]}   # 2 represent the tumor type 2 and 4 is the other tumor, from the breast cancer
    test_set     = {2:[] ,4:[]}
    train_data   = full_data[:-int(test_size*len(full_data))]  # -int has no meaning, we are cutting her from
    test_data    = full_data[-int(test_size*len(full_data)):]  # we are cutting her to

    ############################################################
    #     populate the dictionary to create the data set       #
    ############################################################

    for i in train_data:
        train_set[i[-1]].append(i[:-1])  # the Class (label) (Y) was the last column in the train_data---> full_data,thus -1

    for i in test_data:
        test_set[i[-1]].append(i[:-1])

    " to check everything is in proportion"
   # print(test_size*len(full_data))
   # print(len(full_data),len(train_data),len(test_data))

    ############################################################
    #     pass the info now to our defined algorithm           #
    ############################################################

    correct = 0
    total   = 0

    for group in test_set:               # for each group which they are 2 groups (2) and (4)
        for data in test_set[group]:     # in each group now go inside the list of features
            vote, confidence = k_nearest_neighbors(train_set,data, k=3)   # this is another value you can use k=5
            if group == vote:
                correct += 1
            # else:
            #     #print(confidence)
            total +=1

    #print('Accuracy:', correct/total)
    accuracies.append(correct/total)

print(sum(accuracies)/len(accuracies), 'is the Accuracy of our own K-nearest Neighbor algorithm from  ')
print(30*'#')



accuracies2 = []
for i in range(no_of_checking):
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
    accuracies2.append(accuracy)
    #print(accuracy)
print(sum(accuracies2)/len(accuracies2),'is the Accuracy of K-nearest Neighbor algorithm from Sk-learn ')




