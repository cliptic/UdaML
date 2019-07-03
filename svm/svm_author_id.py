#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

print("preprocess done")
#########################################################
### your code goes here ###

# sets time to current time at the start of training
t0 = time()
from sklearn.svm import SVC
print("SVC imported")
clf = SVC(kernel="linear")
clf.fit(features_train, labels_train) 
print("SVC fitted")
# estimates time of training:
print("training time", round(time()-t0, 3), "s")

# sets time to current time at the start of fitting
t0 = time()

pred = clf.predict(features_test)
print(pred)

# estimates time of prediction
print("predicting time", round(time()-t0, 3), "s")

#########################################################
print("Number of mislabeled points out of a total %d points %d")
mislabeledpoints = (labels_test != pred).sum()
print(mislabeledpoints)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print(acc)


accuracy_of_model = (len(labels_test) - mislabeledpoints)/len(labels_test)
print("Accuracy is:", accuracy_of_model)