#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""  
   
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
# sets time to current time at the start of training
t0 = time()
#< your clf.fit() line of code >
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
fitted = gnb.fit(features_train, labels_train)
# estimates time of training:
print("training time", round(time()-t0, 3), "s")

# sets time to current time at the start of fitting
t0 = time()
# fitting
predicted = fitted.predict(features_test)

# estimates time of prediction
print("predicting time", round(time()-t0, 3), "s")

# number of mislabeled points:
print("Number of mislabeled points out of a total %d points %d")
print((labels_test != predicted).sum())

#########################################################


