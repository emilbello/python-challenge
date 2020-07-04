# dependencies
import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

def py_elections(csvreader):

    
    candidates_dict = {}
    for row in csvreader:
        voter_id.append(row[0])
        candidate.append(row[2])

   
   
        candidates_dict = {}
        for nombre in candidate:
            if nombre in candidates_dict:
                candidates_dict[nombre] += 1
            else:
                candidates_dict[nombre] = 1
    
    for k in candidates_dict:
        candidato = str(k)
        pct_votos = "{:.3%}".format(candidates_dict[k]/total_votes)
        votos = candidates_dict[k]
        #if candidates_dict[k] == max(candidates_dict[k]):
        #    winner = str(k)
    poll_results = f'{candidato}: {pct_votos} ({votos})'
    

    #The percentage of votes each candidate won: for each key, the pct

    #The total number of votes each candidate won: sum by key
    #The winner of the election based on popular vote.: higher sum.
    electionstext = f'''Election Results")
    -------------------------
    Total Votes: {total_votes}
    -------------------------
    {poll_results}
    {candidates_dict}
    
    
    -------------------------
    Winner: 
    -------------------------'''
    return electionstext

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

