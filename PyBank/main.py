
# import dependencies
import os
import csv
# Set path for file
csvpath = os.path.join('Resources','budget_data.csv')

# the functions takes csvreader as a parameter and extracts three lists:
# date, profit/losses, and the change.
# Change list will allow finding the max and min change val and date indexes
def py_analysis(csvreader):
    
    month_year = []
    p_l = []
    change = []
    previous_pl = 0
    for row in csvreader:
        month_year.append(row[0])
        p_l.append(int(row[1]))
        change.append(int(row[1])-previous_pl)
        previous_pl = int(row[1])
    
    # evaluate the total profit by sum of all values in the P&L list
    profit_total = sum(p_l)
    # obtain the number of months by taking the lenght of the month list
    month_total = len(month_year)
    # the profit changed all but the first month, since the first
    # month doesnt count, we use total months - 1
    # average total shortcut by using the P&L firstlast values (index [0] and [-1])
    average_change = round(( p_l[-1] - p_l[0] )/(month_total - 1 ), 2)
            
    # obtain the max and min change.
    greatest_inc = max(change) 
    greatest_dec = min(change)

    # print results. Obtain the months index by using the index method change.index(greatest_inc/dec)
    alltext = f'''Financial Analysis
----------------------------
Total Months: {month_total} 
Total: ${profit_total} 
Average Change: ${average_change}
Greatest Increase in Profits: {month_year[change.index(greatest_inc)]} (${greatest_inc})
Greatest Decrease in Profits: {month_year[change.index(greatest_dec)]} (${greatest_dec})'''
    
    return alltext

# with open read the file path an assing it to csvfile
with open(csvpath) as csvfile:

    # use csv reader by specifyng the variable that holds the content (csvfile) and delimiter 
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the headers
    next(csvreader)

    # run the function for the budget data analysis and assign the output to a variable
    py_analysis_output = py_analysis(csvreader)
    # print the message to the terminal 
    print(py_analysis_output)
    
    # create path for output file
    data_output = os.path.join('analysis', 'py_analysis.txt')

    # create a write a text file with the analysis.
    with open(data_output, 'w', newline="") as text:
        
        text.write(py_analysis_output)
        text.close()