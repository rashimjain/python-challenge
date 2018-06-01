# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV's
import csv

csvpath = os.path.join('raw_data','employee_data1.csv')

# Part 1 - Calculate total number entries in the dataset
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
 #   total_entries = sum(1 for line in open(csvpath))-1

# print(total_entries)

# A Python Dictionary to translate US States to Two letter codes
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Part 2 - Extracting data to lists

empid = []
name =[]
DOB = []
SSN =[]
state =[]

with open(csvpath, newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    next(data)
    
    for row in data:
        empid.append(row[0])
        name.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        state.append(row[4])

# Part 3 - Splitting the names

firstname = []
lastname = []

a = len(name) 
for b in range (0,a):
    c = name[b]
    d = c.split()
    e = str(d[0])
    f = str(d[1])
    firstname.append(e)
    lastname.append(f)
        

# Part 4 - Reformatting Date
DOB_formatted = []
a = len(DOB) 
for b in range (0,a):
    c = DOB[b]
    d = c.split("-")
    year = str(d[0])
    month = str(d[1])
    day = str(d[2])
    new_date = month + "/"+ day + "/" + year 
    DOB_formatted.append(new_date)

        
# Part 5 - Converting the SSN format to "***-**-1234"
extractSSN =[]
g = len(SSN)

for h in range (0, g):
    i = SSN[h]
    j = i[-4:]
    k = "***-**-" + str(j)
    extractSSN.append(k)
    
# Part 6 - Converting states to short format
state_abb =[]

l = len(state)
for m in range (0, l):
    n = state[m]
    o = us_state_abbrev[n]
    p = str(o)
    state_abb.append(p)
        
    
# Zip all three lists together into tuples
combine_data = zip(empid, firstname,lastname, DOB_formatted, extractSSN, state_abb)

# save the output file path
output_file = os.path.join("output.csv")

# open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

 #   Create a header row
    writer.writerow(["Emp-ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # write the zipped object to the csv file using `writer.writerows`
    writer.writerows(combine_data)