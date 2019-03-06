import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    candList = []
    first_row = next(csvreader)
    candList.append({"name": first_row[2], "votes":1})
    
    for row in csvreader:
        added = False
        for cand in candList:
            if (cand["name"] == row[2]) & (added == False):
                cand["votes"] += 1
                added = True
                print("same name")
            elif (cand["name"] != row[2]) & (added == False):
                candList.append({"name": row[2], "votes":1})
                print("diff name")
                added = True
                
    
    print(candList)
    
   
    
