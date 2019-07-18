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

    #create an array of squared errors
    squared_errors = []
    n = 0
    for i in predictions:
        squared_errors.append((predictions[n] - net_worths[n])**2)
        n += 1

    # Function returns a list of indexes 
    # for a percentage of largest elements of a list
    def Nmaxelements(list1, percent): 
        indexes = []
        N = int(len(list1)/100*percent)
        for i in range(N):
            max1 = 0  
            for j in range(len(list1)):      
                if list1[j] > max1: 
                    max1 = list1[j]; 
                    m = j
            list1[m] = 0
            indexes.append(m) 
        return indexes
    indexlist = Nmaxelements(squared_errors, 10)    

    for i in range(len(predictions)):
        if i not in indexlist:
            tuple_n = (ages[i], net_worths[i], squared_errors[i])
            cleaned_data.append(tuple_n)
    
    return cleaned_data
