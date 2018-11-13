#parking tickets

import pandas as pd

#get the name of the csv file 
file = input("Enter name of csv file: ")

#ask the user for an attribute (column header) to seach by
attribute = str(input("Input an attribute: "))

#read file as csv file
inputFile = pd.read_csv(file)

#print the dataframe
#prints the top 10 values
print(inputFile[attribute].value_counts()[:10])

