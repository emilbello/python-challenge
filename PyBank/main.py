
# import dependencies
import os
import csv
# Set path for file
csvpath = os.path.join('Resources','budget_data.csv')
# define the lists that will be used in the function

# define the functions that takes as parameters two lists, date and profit/losses 
def py_analysis(monthyear, p_and_l):
    
    profit_total = sum(p_and_l)
    month_total = len(monthyear)
    # how many times the profit changed if we have X total transactions. Is X - 1.
    # obtain the first and last values with index [1] and [-1]
    average_change = round(( p_and_l[0] - p_and_l[-1] )/(month_total - 1 ), 2)
    greatest_inc = max(p_and_l)
    greatest_dec = min(p_and_l)
    

    # print results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {month_total}")
    print(f"Total: ${profit_total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {monthyear[p_and_l.index(greatest_inc)]} (${greatest_inc})")
    print(f"Greatest Decrease in Profits: {monthyear[p_and_l.index(greatest_dec)]} (${greatest_dec})")

# with open read and get lists and functions to work
with open(csvpath) as csvfile:

    # use csv reader by specifyng the variable that holds the content and delimiter 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    month_year = []
    p_l = []
    for row in csvreader:
        month_year.append(row[0])
        p_l.append(int(row[1]))
       
    print(py_analysis(month_year, p_l))
    
    