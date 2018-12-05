import os
import csv

#create path
#budget_dt= os.path.join("budget_data.csv")
budget_dt= os.path.join("C:/Users/admin/Documents/python-challenge","budget_data.csv")
print(budget_dt)

# Declared/set variable and set them to 0
total_months = 0
total_PL = 0
first_mnth = 0
last_mnth = 0.0
prev_mnth = 0.0
monthlyPLChng =0
avgPLChange=0
avgChng=0
linenum = 0
max_avgChng=0
min_avgChng=0
#great_incr = 0
##great_incr_mon = ""
#great_decr_mon = ""

#create lists to store Profit/Loss change
avgMonthlyChngPL = []

# read csv file

with open(budget_dt, "r", newline="") as csvfile:

    rownum = csvfile.readlines()

    total_months = len(rownum) - 1

    csvfile.seek(0,0)

    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        print(row)
#count total PL in csv file
        total_PL += float(row[1])
        #create a variable that will count the PL change
        monthlyPLChng = int(row[1]) - prev_mnth
        prev_mnth = int(row[1])
        #add changes in new list
        avgMonthlyChngPL.append(monthlyPLChng)
        avgPLChange = round(sum(avgMonthlyChngPL)/total_months)

        if (linenum == 0):
            first_mnth = float(row[1])
            prev_mnth = float(row[1])
        elif (linenum == total_months-1):
            last_mnth = float(row[1])
        if  (linenum >0):
            avgChng.append((row[0] , float(row[1]) - prev_mnth))
            prev_mnth = float(row[1])
            max_avgChng = max(avgChng, key=lambda item: item[1])
            min_avgChng = min(avgChng, key=lambda item: item[1])


            linenum += 1
avg_Chng = (last_mnth - first_mnth)/ (total_months-1)
print(total_months)
print(total_PL)
print(avgPLChange)
print(avgMonthlyChngPL)
print (avgChng)
print(max_avgChng)
Print(min_avgChng)
