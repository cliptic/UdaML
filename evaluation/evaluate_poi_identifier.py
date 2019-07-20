#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.metrics import confusion_matrix
from sklearn import metrics

data_dict = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]
data = featureFormat(data_dict, features_list)
sort_keys = '../tools/python2_lesson14_keys_unix.pkl'
labels, features = targetFeatureSplit(data)



### your code goes here 

### it's all yours from here forward!  
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, pred)
print(acc)

print(sum(pred))
print(sum(labels_test))
print(len(labels_test))
print(25/29)

n=0
truepositives = 0
truenegatives = 0
falsepositives = 0
falsenegatives = 0
for i in pred:
	if (pred[n] == labels_test[n]) and pred[n] == 1:
		truepositives += 1
	elif (pred[n] == labels_test[n]) and pred[n] == 0:
		truenegatives += 1
	elif (pred[n] != labels_test[n]) and pred[n] == 1:
		falsepositives += 1
	else:
		falsenegatives += 1
	n += 1

print("True positives:", truepositives)
print("True negatives:", truenegatives)
print("False positives:", falsepositives)
print("False negatives:", falsenegatives)

print(confusion_matrix(labels_test, pred))

print("Precision score:", metrics.precision_score(pred, labels_test))
print("Recall score:", metrics.recall_score(pred, labels_test))

# made- up data questions
A_predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
A_true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

print(confusion_matrix(A_true_labels, A_predictions))
print("Precision score:", metrics.precision_score(A_true_labels, A_predictions))
print("Recall score:", metrics.recall_score(A_true_labels, A_predictions))