# dependencies
import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

def py_elections(voter_id, candidate):

    #The total number of votes cast: count id
    total_votes = len(voter_id)
    #A complete list of candidates who received votes: count uniques 
    #candidates = set(candidate)
    
    from collections import Counter
    print(Counter(candidate).keys()) # equals to list(set(candidate))
    print(Counter(candidate).values()) # counts the elements' frequency

    #The percentage of votes each candidate won: for each key, the pct

    #The total number of votes each candidate won: sum by key
    #The winner of the election based on popular vote.: higher sum.
    electionstext = f'''Election Results")
    -------------------------
    Total Votes: {total_votes}
    -------------------------

    -------------------------
    Winner: 
    -------------------------'''
    return electionstext

with open(csvpath) as csvfile:

    # use csv reader by specifyng the variable that holds the content and delimiter 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    voter_id = []
    candidate = []
    for row in csvreader:
        voter_id.append(row[0])
        candidate.append(row[2])
    
    py_elections(voter_id, candidate)
    
    # create path for output file
    #data_output = os.path.join('analysis', 'py_elections.txt')

    #with open(data_output, 'w', newline="") as text:
        
       # text.write(str(py_elections) + '\n')
       # text.close()

