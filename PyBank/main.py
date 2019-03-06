import os

import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    
#get row count in order to get total # of months
    net_profit = 0
    row_count = 0
    prev = 0 
    prof_change = 0
    total_change = 0
    max_increase = 0
    max_decrease = 0
    


    for row in csvreader:
        row_count += 1
        net_profit += int(row[1])
        if row_count != 1:
            prof_change = (int(row[1]) - int(prev))
            total_change += prof_change
            if prof_change > max_increase:
                max_increase = prof_change
                max_increase_name = row[0]
            elif prof_change < max_decrease:
                max_decrease = prof_change
                max_decrease_name = row[0]
        prev = row[1]

 

    
    


#get total net profit by looping through each row and adding to a total net_profit tracker
    
    
    


    print("Financial Analysis")
    print("------------------") 
    print("Total Months: ",row_count, sep="")
    print("Total: $",net_profit,sep="")
    print(f"Average Change: ${(total_change/(row_count - 1)):.2f})")
    print(f"Greatest Increase in Profits: {max_increase_name} (${max_increase})")
    print(f"Greatest Decrease in Profits: {max_decrease_name} (${max_decrease})")
