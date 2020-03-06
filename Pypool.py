import os
import operator
import csv
import json # to format the print of the dictionary


dir_path = os.path.dirname(__file__)
csvpath = os.path.join(dir_path,"PyPoll.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter="," )
    # Make sure the loop will not count the first line 
    next(csvreader) 

    total = 0
    i = 0
    r = 0
    winner = 0
    pct = []
    mdict = {}
    v = list(mdict.values())
    k = list(mdict.keys())
# Make a loop to get the ammount of votes.
# Then go through the row[2], to give me the keys and values to my dictionary
    for row in csvreader:  
        total += 1
        if row[2] not in mdict:
            mdict[row[2]] = 1
        else:
            mdict[row[2]] += 1
#Get the percentages numbers and round them       
    for k,v in mdict.items():
        i = v * 100 / total
        pct.append(i)
        r = [round(num, 2) for num in pct]     

    print(f"Total Votes: {total}")
    print(f"Percentages: {r}%")
    print(json.dumps(mdict, indent=4))
    print(f"Winner: {max(mdict.items(), key=operator.itemgetter(1))}")
    
    
    