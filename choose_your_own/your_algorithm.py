#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.ensemble import AdaBoostClassifier
from time import time
clf = AdaBoostClassifier()

'''# code to use 10% of training data
features_train = features_train[:int(len(features_train)/10)] 
labels_train = labels_train[:int(len(labels_train)/10)] 
print("using 10\% of training data") '''

t0 = time()
clf = clf.fit(features_train, labels_train)
print("training time", round(time()-t0, 3), "s")

t0 = time()
pred = clf.predict(features_test)
print("Prediction time", round(time()-t0, 3), "s")

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print("accuracy of AdaBoost model: ", acc)

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
    print("Printing was not initiated")


from sklearn.ensemble import RandomForestClassifier
from time import time
clf = RandomForestClassifier()

'''# code to use 10% of training data
features_train = features_train[:int(len(features_train)/10)] 
labels_train = labels_train[:int(len(labels_train)/10)] 
print("using 10\% of training data") '''

t0 = time()
clf = clf.fit(features_train, labels_train)
print("training time", round(time()-t0, 3), "s")

t0 = time()
pred = clf.predict(features_test)
print("Prediction time", round(time()-t0, 3), "s")

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print("accuracy of Random Forest model: ", acc)