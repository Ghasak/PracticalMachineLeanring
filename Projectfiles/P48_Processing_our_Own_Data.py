''' - Originally this file here named as "create_sentiment_featureset
        and the README_P48 where the details of this script"'''

import nltk
from nltk.tokenize import word_tokenize
import numpy as np
import random
import pickle
from collections import Counter
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
hm_lines = 100000


def create_lexicon(pos,neg):
    lexicon = []
    for fi in [pos, neg]:
        with open(fi, 'r') as f:
            contents = f.readlines()
            for l in contents[:hm_lines]:
                all_words = word_tokenize(l.lower()) # Method for lower cases.
                lexicon += list(all_words)


    lexicon = [lemmatizer.lemmatize(i) for i in lexicon]
    w_counts = Counter(lexicon)
    # w_counts = {'the':4535, 'and':2312 ...etc} we are expecting the results to be a dictionary.
    l2 = []
    for w in w_counts:
        if 1000 > w_counts[w] > 50: # We are saying not the super common words, like "the", "and",..etc.
            l2.append(w)
    print(len(l2))
    return l2

# =================================================================================

def sample_handling(sample, lexicon, classification):
    featureset = []

    with open(sample, 'r') as f:
        contents = f.readlines()
        for l in contents[:hm_lines]:
            current_words = word_tokenize(l.lower())
            current_words = [lemmatizer.lemmatize(i) for i in current_words]
            features = np.zeros(len(lexicon))
            for word in current_words:
                if word.lower() in lexicon:
                    index_value = lexicon.index(word.lower())
                    features[index_value] +=1
            features = list(features)
            featureset.append([features, classification])

    return featureset


# =================================================================================


def create_feature_sets_and_labels(pos, neg, test_size= 0.1):
    lexicon = create_lexicon(pos,neg)
    features = []
    features += sample_handling(pos, lexicon,[1,0])
    features += sample_handling(neg, lexicon,[0,1])
    random.shuffle(features)

    features = np.array(features)

    testing_size = int(test_size*len(features))

    train_x = list(features[:,0][:-testing_size])
    train_y = list(features[:,1][:-testing_size])
    test_x  = list(features[:,0][-testing_size:])
    test_y  = list(features[:,1][-testing_size:])

    return train_x,train_y,test_x,test_y

import os
CURRENT_DIR = os.getcwd()
# Where our positive files
POSITIVE_DIR = os.path.join(CURRENT_DIR,'resources/positiveData.txt')
# print(POSITIVE_DIR)
# Where our negative files
NEGATIVE_DIR = os.path.join(CURRENT_DIR,'resources/negativeData.txt')
# print(NEGATIVE_DIR)
# Export Directory:
SENTIMENT_DIR = os.path.join(CURRENT_DIR,'resources/sentiment_set.pickle')

def main():
    train_x,train_y,test_x,test_y = create_feature_sets_and_labels(POSITIVE_DIR,NEGATIVE_DIR)
	# if you want to pickle this data:
    with open(SENTIMENT_DIR,'wb') as f:
        pickle.dump([train_x,train_y,test_x,test_y],f)

if __name__ == '__main__':
	main()
