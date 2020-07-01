
# import dependencies
import os
import csv
# Set path for file
csvpath = os.path.join('Resources','budget_data.csv')
# define the lists that will be used in the function

# define the functions that takes as parameters two lists, date and profit/losses 
def py_analysis(monthyear, p_and_l):
    
    # evaluate the total profit by sum of all values
    profit_total = sum(p_and_l)
    # obtain the number of months by getting the lenght of the month list
    month_total = len(monthyear)
    # how many times the profit changed if we have X total transactions. Is X - 1, since the first one doesnt count (no change).
    # obtain the first and last values from the P&L ist with index [0] and [-1]
    average_change = round(( p_and_l[-1] - p_and_l[0] )/(month_total - 1 ), 2)
    
    
    #p_and_l_previous = 0
    #change = []
    #for i in p_and_l:
    #    val_change = ( p_and_l[i] - p_and_l_previous )
    #    change.append(val_change)
    #    p_and_l_previous = p_and_l[i]
    
    # obtain the max and min change.
    greatest_inc = max(change) 
    greatest_dec = min(change)

    # print results. Obtain the months index by using the index method change.index(greatest_inc/dec)
    alltext = f'''Financial Analysis
    ----------------------------
    Total Months: {month_total} 
    Total: ${profit_total}
    Average Change: ${average_change}
    Greatest Increase in Profits: {monthyear[change.index(greatest_inc)]} (${greatest_inc})
    Greatest Decrease in Profits: {monthyear[change.index(greatest_dec)]} (${greatest_dec})'''
    
    return alltext

# with open read and get lists and functions to work
with open(csvpath) as csvfile:

    # use csv reader by specifyng the variable that holds the content and delimiter 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)


    month_year = []
    p_l = []
    change = []
    previous_pl = 0
    for row in csvreader:
        month_year.append(row[0])
        p_l.append(int(row[1]))
        change.append(int(row[1])-previous_pl)
        previous_pl = int(row[1])
    
    py_analysis_output = py_analysis(month_year, p_l)
    print(py_analysis_output)
    
    # create path for output file
    data_output = os.path.join('analysis', 'py_analysis.txt')

    with open(data_output, 'w', newline="") as text:
        
        text.write(py_analysis_output)
        text.close()
    