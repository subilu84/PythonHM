import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path, "Bank.csv")

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    total_months = 0 
    total = 0
    increase = ["", 0]
    decrease = ["", 9999]
    rown = 0
    i = 0
    p = 0
    average = 0
    change_list = []
    # Change_list = [867884, 116771,-662642..]

    
# Made the loop to get the net total os the amount Profit/Losses, total of months and the average change
    for row in csvreader:
        total += int(row[1])
        total_months += 1
# The average change was made subtracting the 1st line for 2nd line and adding this value in the change list
        change = int(row[1]) - p
        p = int(row[1])
        change_list.append(change)
        lenght_list = len(change_list) - 1
 # Once I had all the values in the change list, the if statement was made to find the gratest
 # and the smallest number and also the month     
        if change > increase[1]:
            increase[1] = change
            increase[0] = row[0]
            # or max(change_list)
        if change < decrease [1]:
            decrease[1] = change
            decrease[0] = row[0]
            # or min(cahnge_list)
    average = sum(change_list[1:]) / lenght_list

    print(f"Total: {total}")
    print(f"Total of months: {(total_months)}")
    print(f"Average Change: {average:.2f}")
    print(f"Greatest increase Average: {increase[0], increase[1]}")
    print(f"Greatest decrease Average: {decrease[0], decrease[1]}")


  
   
    