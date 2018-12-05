
# Import the csv data for
import os
import csv
# Open the cvs file and read data line
budget_dt= os.path.join("C:/Users/admin/Documents/python-challenge","budget_data.csv")

# with open csv file
Total_PL=0.0
with open("budget_dt", "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    for row in csvreader:
    #Print variable from csv file cnt
    # The total number of months included in the dataset or
        #row_count=len(csvreader)
     Total_Months=sum(1 for row csvreader)
     #

     #The total net amount of "Profit/Losses" over the entire period
     Total_PL += float(row[1])

    #The average change in "Profit/Losses" between months over the entire period










    results.append("Total_Months:" + "" + str(len(csvreader)-1))

    csvreader=budget_dt


def count=("date"):
    line_cnt=total_PL= first_mon_PL = last_mon_PL=0
    total=sum(row)
    cnt=len(row)
    return(total/cnt)
    Curr_month= []
    prev_month=[]
    Date=[]
    Date=month




