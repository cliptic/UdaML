#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""


import pickle
import pandas as pd 

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))

print("There are", len(enron_data), "people in the dataset")
print(type(enron_data))

# Count number of features
my_list = []
for key,value in enron_data['METTS MARK'].items() :
    my_list.append(key)
print("Features for every person:")
print(my_list)
print("There are", len(my_list), "Features for every person")

# How many POIs? (Persons of interest)

my_list_people = []
for key,value in enron_data.items() :
    my_list_people.append(key)
# print(my_list_people)

n=0
for key in my_list_people:
	if enron_data[key]["poi"] == 1 :
		n += 1
print("There are", n, "people, listed as POIs")

print("Value of stocks belonging to James Prentice:", enron_data['PRENTICE JAMES']['total_stock_value'])