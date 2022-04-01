#PyBank main
# import csv, create path to csv
from __future__ import division
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # f.write("CSV Header: " + str(csv_header)
    counter = 0
    net_amount = 0
    change = 0
    previous_row = 0
    net_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    increase_date = 0
    decrease_date = 0
    # Read each row of data after the header
    for row in csvreader:
        
        if csvreader.line_num == 2:
            previous_row = int(row[1])

        counter = counter + 1
        net_amount = net_amount + int(row[1])
        change = int(row[1]) - previous_row
        net_change = net_change + change
        previous_row = int(row[1])
        date = (row[0])

        if change > greatest_increase:
            greatest_increase = change
            increase_date = date
        if change < greatest_decrease:
            greatest_decrease = change
            decrease_date = date


# f.write average change
average_change = net_change / (counter - 1)

# f.write answer
with open('analysis/PyBank_Analysis.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("--------------------------\n")
    f.write("Total Months: " + str(counter) + "\n")
    f.write("Total: $" + str(net_amount) + "\n")
    f.write("Average Change: $" + str(round(average_change,2)) + "\n")
    f.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")\n")
    f.write("Greatest Decrease in Profits: " + str(decrease_date) +  " ($" + str(greatest_decrease) + ")\n")