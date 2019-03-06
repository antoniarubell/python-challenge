#dependencies
import os
import csv

#file path
csvpath = os.path.join('election_data.csv')

#read file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#initialize variables
    candidates = {}
    total_votes = 0

#loop through rows
    for row in csvreader:
        total_votes += 1  #find total votes by adding a count for each row
        if row[2] in candidates:   #check for existing candidate dictionary
            candidates[row[2]]['votes'] += 1    #if exists, add vote
        else:
            candidates[row[2]] = {'votes': 1, 'name': row[2]}     #if not, create dictionary
   
    

#printing results
    print("Election Results")
    print("------------------") 
    print(f"Total Votes: {total_votes}")
    print("------------------") 


    max_votes = 0            #to find the winning candidate   
    for key in candidates:       #loop through candidate dictionary
       
       #print each candidate, % of total votes, and vote #
        print(key,": ",format(candidates[key]['votes']/total_votes*100, '.3f'),"% (",candidates[key]['votes'],")", sep="") 
        
        #find the winner
        if candidates[key]['votes'] > max_votes:
            max_votes = candidates[key]['votes']
            winner = key

    print("------------------") 
    print("Winner:",winner)
    print("------------------") 




   
    
