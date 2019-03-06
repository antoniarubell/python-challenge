import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    candidates = {}
    total_votes = 0
    
    for row in csvreader:
        total_votes += 1
        if row[2] in candidates:
            candidates[row[2]]['votes'] += 1
        else:
            candidates[row[2]] = {'votes': 1, 'name': row[2]}
   
    


    print("Election Results")
    print("------------------") 
    print(f"Total Votes: {total_votes}")
    print("------------------") 
   
    max_votes = 0
    for key in candidates:
        #print(f'{key}: {candidates[key]['votes']}')
        print(key,": ",format(candidates[key]['votes']/total_votes*100, '.3f'),"% (",candidates[key]['votes'],")", sep="")
        
        if candidates[key]['votes'] > max_votes:
            max_votes = candidates[key]['votes']
            winner = key

    print("------------------") 
    print("Winner:",winner)
    print("------------------") 




   
    
