import os
import csv

election_dt= os.path.join("C:/Users/admin/Documents/python-challenge","election_data.csv")
print(election_dt)

# create the lists and dictionary

total_vote = 0
candidatelist = []
vote_cnt = {}
vote_percent = {}

#Open and read csv file
with open(election_dt, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    for row in csvreader:
        #csvfile.seek(0,0)
     #rownum = csvfile.readlines()
     total_vote = total_vote + 1
     if row[2] not in candidatelist :
        candidatelist.append(row[2])
        vote_cnt[row[2]] = 1
     else:
        vote_cnt[row[2]] = vote_cnt[row[2]] + 1
#calculate percentage of votes each candidate won
for key, value in vote_cnt.items():
    vote_percent[key] = str(round(((value/total_vote)*100),3)) + "% ("+str(value) + ")"
winner=max(vote_cnt, key=vote_cnt.get)

#print(total_vote)
#print(vote_percent)
#print(winner)

print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_vote))
print("-------------------------------------")
for key row  in candidatelist:
    print(key + ": " + str(vote_percent[key]) + "% (" + str(value) + ")")
    print("-------------------------------------")
    print("Winner: " + winner)
    print("-------------------------------------")

# creating new text file
outputfile = open("Output/results.txt", "w")

# writing the new file
outputfile.write("Election Results \n")
outputfile.write("------------------------------------- \n")
outputfile.write("Total Votes: " + str(total_vote) + "\n")
outputfile.write("------------------------------------- \n")
for key, value in candidatelist.items():
    outputfile.write(key + ": " + str(vote_percent[key]) + "% (" + str(value) + ") \n")
outputfile.write("------------------------------------- \n")
outputfile.write("Winner: " + winner + "\n")
outputfile.write("------------------------------------- \n")
