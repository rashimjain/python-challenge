    # First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV's
import csv

csvpath = os.path.join('raw_data','election_data_1.csv')

# Part 1 - Calculate total number of votes
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    total_votes = sum(1 for line in open(csvpath))-1
# print(total_votes)

# Part 2

Voterid = []
County =[]
Unique_Candidate = []


with open(csvpath, newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    next(data)
    
#    for row in data:
 #       Voterid.append(row[0])
  #      County.append(row[1])
   #     Candidate.append(row[2])
        
    for row in data:
        if row[2] not in Unique_Candidate:
            Unique_Candidate.append(row[2]) 

# print (Unique_Candidate)

# Part 3, 4 , 5

Voterid = []
County =[]
Candidate = []
Unique_Candidate = []

with open(csvpath, newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    next(data)
    
    for row in data:
        Voterid.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        if row[2] not in Unique_Candidate:
            Unique_Candidate.append(row[2])

a = len(Unique_Candidate)

votes_recieved = []
percentage_votes =[]

print ("Election Results")
print ("------------------------")
print ("Total Votes: " + str(total_votes))
print ("------------------------")

for b in range (0,a):
    c = Candidate.count(Unique_Candidate[b])
    d = float((c / total_votes)*100)
    e = round(d,2)
    votes_recieved.append(c)
    percentage_votes.append(e)
    print (Unique_Candidate[b] + ": " + str(e) + "%" + "(" + str(c) + ")")

print ("------------------------")
e = votes_recieved.index(max(votes_recieved))
winner = Unique_Candidate[e]
print ("Winner: " + winner)
print ("------------------------")

# Part 7 - Exporting the results to text  file
import sys
filename  = open('PyPoll_Summary_Output.txt','w')
sys.stdout = filename

Voterid = []
County =[]
Candidate = []
Unique_Candidate = []

with open(csvpath, newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    next(data)
    
    for row in data:
        Voterid.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        if row[2] not in Unique_Candidate:
            Unique_Candidate.append(row[2])

a = len(Unique_Candidate)

votes_recieved = []
percentage_votes =[]

print ("Election Results")
print ("------------------------")
print ("Total Votes: " + str(total_votes))
print ("------------------------")

for b in range (0,a):
    c = Candidate.count(Unique_Candidate[b])
    d = float((c / total_votes)*100)
    e = round (d,2)
    votes_recieved.append(c)
    percentage_votes.append(e)
    
for x,y,z in zip(Unique_Candidate,percentage_votes,votes_recieved):
    print (str(x) +": "+ str(y) +"% " + "(" + str(z) +")")

print ("------------------------")
e = votes_recieved.index(max(votes_recieved))
winner = Unique_Candidate[e]
print ("Winner: " + winner)
print ("------------------------")