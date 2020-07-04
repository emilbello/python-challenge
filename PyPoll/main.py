import os
import csv

# set path to file
csvpath = os.path.join('Resources','election_data.csv')

# the function takes csvreader as a parameter and counts the total votes and 
# extract the candidates to a dictionary while counting the votes for each (by adding up
# the every time the candidate names repeats)
def py_elections(csvreader):

    total_votes = 0
    candidates_count = {}
    for row in csvreader:
        total_votes = total_votes + 1
        
        nombre = row[2]
        if nombre not in candidates_count:
            candidates_count[nombre] = 1
        else:
            candidates_count[nombre] += 1
    
# create a for loop to extract the three fields required in the answer and store
# it in variables winner_name and poll_results
    winner = 0
    winner_name = ''
    poll_results = ''
    for k, v in candidates_count.items():
        poll_results += f'{k}: {"{:.3%}".format(v/total_votes)} ({v}) \n'
        if v > winner:
            winner = v
            winner_name = k
# print results.
    alltext = f'''Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{poll_results}-------------------------
Winner: {winner_name}
-------------------------'''
    return alltext

with open(csvpath) as csvfile:

    # use csv reader by specifyng the variable that holds the content and delimiter 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

# run the function for the elections analysis and assign the output to a variable
    py_elections_output = py_elections(csvreader)
    
    print(py_elections_output)
    
    #create path for output file
    data_output = os.path.join('analysis', 'py_elections.txt')

    # create and write a text file with the analysis
    with open(data_output, 'w', newline="") as text:
        
       text.write(py_elections_output)
       text.close()