# dependencies
import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

def py_elections(csvreader):

    total_votes = 0
    candidates_count = {}
    for row in csvreader:
        total_votes = total_votes + 1
        
        nombre = row[2]
        if nombre in candidates_count:
            candidates_count[nombre] += 1
        else:
            candidates_count[nombre] = 1

    
    for k, v in candidates_count.items():
        #pct_votos = "{:.3%}".format(k/total_votes)
        poll_results = print(f'{k}: ({v})')
        
    alltext = f'''Election Results")
-------------------------
Total Votes: {total_votes}
-------------------------
{poll_results} 
{k} {v}
-------------------------
Winner:
-------------------------'''
    return alltext

with open(csvpath) as csvfile:

    # use csv reader by specifyng the variable that holds the content and delimiter 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    py_elections_output = py_elections(csvreader)
    
    print(py_elections_output)
    
    # create path for output file
    #data_output = os.path.join('analysis', 'py_elections.txt')

    #with open(data_output, 'w', newline="") as text:
        
       # text.write(py_elections_output)
       # text.close()

