import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path, "Election.Data.csv")

output_file = os.path.join(dir_path, "HW_Output.csv")

with open("Election.Data.csv", 'r') as csvfile: 
    csvreader = csv.reader(csvfile) 
       
    fields = csvreader.next()  
    for row in csvreader: 
        rows.append(row) 
  
    print("Total no. of rows: %d"%(csvreader.line_num)) 

def unique(list1): 
  
    unique_list = ["Election.Data.csv"] 
       
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x) 
    for x in unique_list: 
        print(x) 
print("the unique values from 1st list is") 
unique(list1)

for ele in range(0, len(list1)): 
    total = total + list1[ele] 
  
print("Sum of all elements in given list: ", total)