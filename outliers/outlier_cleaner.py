#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    squared_errors = []
    n = 0
    for i in predictions:
        squared_errors.append((predictions[n] - net_worths[n])**2)
        n += 1

    m = 0
    for i in predictions:
        

    ### your code goes here

    
    return cleaned_data
