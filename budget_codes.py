# Import the csv data for
import os
import csv
# Open the cvs file and read data line

#budget_dt= os.path.join("budget_data.csv")
budget_dt= os.path.join("C:/Users/admin/Documents/python-challenge","budget_data.csv")
print(budget_dt)

Total_PL = first_mnth = last_mnth = 0.0
prev_mnth = 0.0
linenum = 0

avgChng = []

# with open csv file

with open(budget_dt, "r", newline="") as csvfile:

	rownum = csvfile.readlines()

	total_months = len(rownum) - 1

	csvfile.seek(0,0)

	csvreader = csv.reader(csvfile, delimiter=",")
	# goto to data line

	next(csvreader)
  for row in csvreader:
    print (row)
    Total_PL += float(row[1])
    if (linenum == 0):
      first_mnth = float(row[1])
      prev_mnth = float(row[1])
    elif (linenum == total_months-1):
      last_mnth = float(row[1])
    if (linenum >0):
      avgChng.append((row[0] , float(row[1]) - prev_mnth))
      prev_mnth = float(row[1])

    linenum += 1
avg_chng = (last_mnth - first_mnth)/ (total_months-1)
