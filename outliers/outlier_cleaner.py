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
    print(Nmaxelements(squared_errors, 10))
        

    ### your code goes here

    
    return cleaned_data
