# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV's
import csv

csvpath = os.path.join('raw_data','budget_data_1.csv')

# Part 1 - Calculate total number  of months in the dataset
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    total_months = sum(1 for line in open(csvpath))-1
# print(total_months)

# Part 2 - Calculate total revenue over period
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    total_revenue = 0
    
    for row in csvreader:
        total_revenue = total_revenue + int(float(row[1]))
    
    # print (total_revenue)

# Part 3 - Calculate average change in revenue between months
Date = []
Revenue =[]
Average_change = [0]


with open(csvpath, newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    next(data)
    
    for row in data:
        Date.append(row[0])
        Revenue.append(row[1])
        
        counter = 0
        y = 0

for counter in range(0, len(Date)-1):    
    y = counter + 1
    rev_change = int(float(Revenue[y]))-int(float(Revenue[counter]))
    Average_change.append(rev_change)

# Zip all three lists together into tuples
combine_data = zip(Date, Revenue, Average_change)

# save the output file path
# output_file = os.path.join("output.csv")

# open the output file
# with open(output_file, "w", newline="") as datafile:
#    writer = csv.writer(datafile)

 #   Create a header row
   # writer.writerow(["Date", "Revenue", "Average Revenue Change"])

    # write the zipped object to the csv file using `writer.writerows`
  #  writer.writerows(combine_data)

a = int(float(sum(Average_change)/len(Average_change)))
# print (a)

# Part 4 - Calculate greatest increase in revenue
b = Average_change.index(max(Average_change))
c = Date[b]
d = max(Average_change)
# print (c,d)

# Part 5 - Calculate greatest decrease in revenue
e = Average_change.index(min(Average_change))
f = Date[e]
g = min(Average_change)
# print (f,g)

# Part 6 - Print Summary
print ("Financial Analysis")
print ("-------------------------------------")
print ("Total Months: "+ str(total_months))
print ("Total Revenue: $"+ str(total_revenue))
print ("Average Revenue Change: $" +str(a))
print ("Greatest Increase in Revenue: "+ c + "($"+str(d)+")")
print ("Greatest Decrease in Revenue: "+ f + "($"+str(g)+")")

# Part 7 - Exporting the results to text  file
import sys
filename  = open('PyBank_Summary_Output.txt','w')
sys.stdout = filename
print ("Financial Analysis")
print ("-------------------------------------")
print ("Total Months: "+ str(total_months))
print ("Total Revenue: $"+ str(total_revenue))
print ("Average Revenue Change: $" +str(a))
print ("Greatest Increase in Revenue: "+ c + "($"+str(d)+")")
print ("Greatest Decrease in Revenue: "+ f + "($"+str(g)+")")

