import os

import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
#initialize tracker variables
    net_profit = 0
    row_count = 0 #to count the # of months
    prev = 0 #to store the previous profit, in order to calculate change from the currnet
    prof_change = 0 #profit change (current profit - prev)
    total_change = 0 #sum of profit change
    max_increase = 0 #max profit change
    max_decrease = 0 #max negative profit change
    


    for row in csvreader:
        row_count += 1 #to count all the months
        net_profit += int(row[1]) #to calc the net profit change across all months
        if row_count != 1:  #to skip the first row, since we're lookign at change in profit
            prof_change = (int(row[1]) - int(prev)) #
            total_change += prof_change
            if prof_change > max_increase:
                max_increase = prof_change
                max_increase_name = row[0]
            elif prof_change < max_decrease:
                max_decrease = prof_change
                max_decrease_name = row[0]
        prev = row[1]

 

    


    print("Financial Analysis")
    print("------------------") 
    print("Total Months: ",row_count, sep="")
    print("Total: $",net_profit,sep="")
    print(f"Average Change: ${(total_change/(row_count - 1)):.2f})")
    print(f"Greatest Increase in Profits: {max_increase_name} (${max_increase})")
    print(f"Greatest Decrease in Profits: {max_decrease_name} (${max_decrease})")
