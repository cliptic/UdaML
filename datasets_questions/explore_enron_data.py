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
print(my_list_people)

PoiPeople=0
for key in my_list_people:
	if enron_data[key]["poi"] == 1 :
		PoiPeople += 1
print("There are", PoiPeople, "people, listed as POIs")

print("Value of stocks belonging to James Prentice:", 
	enron_data['PRENTICE JAMES']['total_stock_value'])

print("Number of messages from Wesley Colwell to POIs:", 
	enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print("The value of stock options exercised by Jeffrey K Skilling:", 
	enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

# Who got the most money?
print("How much money did they get?")
print("SKILLING JEFFREY K:", 
	enron_data['SKILLING JEFFREY K']['total_payments'])
print("LAY KENNETH L:", 
	enron_data['LAY KENNETH L']['total_payments'])
print("FASTOW ANDREW S:", 
	enron_data['FASTOW ANDREW S']['total_payments'])

# No. of people with listed salaries, emails
n=0
for key in my_list_people:
	if enron_data[key]["salary"] != 'NaN' :
		n += 1
print("Number of people with salaries listed:",n)

n=0
for key in my_list_people:
	if enron_data[key]["email_address"] != 'NaN' :
		n += 1
print("Number of people with known email addresses:",n)

# How many people in the E+F dataset 
#(as it currently exists) have “NaN” for their total payments?
# What percentage of people in the dataset as a whole is this?

totalPaymentNaNs = 0
for key in my_list_people:
	if enron_data[key]["total_payments"] == 'NaN' :
		totalPaymentNaNs += 1
print("Number of people with unknown total payment:", totalPaymentNaNs)
print("Percentage of people with no information on total payments:", 
	totalPaymentNaNs/len(my_list_people)*100, "%")

# How many POIs in the E+F dataset have “NaN” 
# for their total payments? 
# What percentage of POI’s as a whole is this?

totalPaymentPoiNaNs = 0
for key in my_list_people:
	if enron_data[key]["poi"] == True and enron_data[key]["total_payments"] == 'NaN':
		totalPaymentPoiNaNs += 1
print("Number of POI people with unknown total payment:", totalPaymentPoiNaNs)
print("Percentage of POI people with no information on total payments:", 
	totalPaymentPoiNaNs/PoiPeople*100, "%")