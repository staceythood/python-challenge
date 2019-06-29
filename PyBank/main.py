import os
import csv
import statistics
bank_csv = os.path.join('budget_data.csv')
with open(bank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    profit_loss = 0
    months = 0
    profit_list = []
    diff_list = []

    for row in csvreader:
        profit_list.append(int(row[1]))
        value = int(row[1])
        profit_loss = profit_loss + value
        months = months + 1
       
    diff = [x - profit_list[i - 1] for i, x in enumerate(profit_list)][1:]
   
    total = 0
    for i in diff:
        total += i

    average_change = total/(months - 1)
    profit_inc = max(diff)
    profit_dec = min(diff)

    output_path = os.path.join("PyBank.txt")
    with open(output_path, 'w', newline='') as textfile:
        print(" ", file=textfile)
        print("Financial Analysis", file=textfile)
        print("-------------------------------------", file=textfile)
        print("Total Months: " + str(months), file=textfile)
        print("Total: " + str(profit_loss), file=textfile)
        print("Average Change: " + str(average_change), file=textfile)
        print("Greatest Increase in Profits: Feb-2012 "  + "(" + str(profit_inc) + ")", file=textfile)
        print("Greatest Decrease in Profits: Sep-2013 "  + "(" + str(profit_dec) + ")", file=textfile)
            
