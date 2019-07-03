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

# ADD FEATURES AS IN LESSON 3.30

''' features_train = features_train[:int(len(features_train)/100)] 
labels_train = labels_train[:int(len(labels_train)/100)] 
print("using 1\% of training data") '''

# add loop for C

from sklearn.svm import SVC
print("SVC imported")
n=0
Cset = [10000]
for i in Cset:
	C_value = Cset[n]
	n += 1
	clf = SVC(kernel="rbf", C = C_value)
	# sets time to current time at the start of training
	t0 = time()
	clf.fit(features_train, labels_train) 
	print("SVC fitted with C value of ", C_value)

	# estimates time of training:
	print("training time", round(time()-t0, 3), "s")

	# sets time to current time at the start of fitting
	t0 = time()

	pred = clf.predict(features_test)
	print(pred)

	# estimates time of prediction
	print("predicting time", round(time()-t0, 3), "s")

	#########################################################
	print("Number of mislabeled points")
	mislabeledpoints = (labels_test != pred).sum()
	print(mislabeledpoints)

	from sklearn.metrics import accuracy_score
	acc = accuracy_score(pred, labels_test)
	print("Accuracy with C value of ", C_value, " is:", acc)