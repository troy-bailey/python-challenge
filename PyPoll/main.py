# Install Modules
import os
import csv
from pathlib import Path

# Setup path to read csv file
csvpath = Path("election_data.csv")

# Set up variables
voteTally = {}
voteCount = 0
winnerName = ""
winnerCount = 0

# Open csv file
with open (csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

# Read the header row
    csv_header = next(csvreader)

# Loop through file
    for row in csvreader:
        voteCount = voteCount + 1

# If the candidate is in the dictionary, add 1 to their tally
        if (row[2] in voteTally):
            voteTally[row[2]] = voteTally[row[2]]  + 1

# If not, initialize the candidate with a tally of 1
        else:
            voteTally[row[2]] = 1

# Set up analysis headers
print("Election Results")
print("-----------------------")
print("Total Votes: " + str(voteCount))
print("-----------------------")
# Loop through the tally and create the datatable
for candidate in voteTally:
    if voteTally[candidate] > winnerCount:
        winner = candidate
        winnerCount = voteTally[candidate]
    print(candidate + " " + "%5.2f"% ((voteTally[candidate]/voteCount)*100) + "% (" + str(voteTally[candidate]) + ")")  
#    print(candidate + " " + str(round(((voteTally[candidate]/voteCount)*100),4)) + "% (" + str(voteTally[candidate]) + ")")
print("-----------------------")
print("Winner: " + winner)
print("-----------------------")

# Output to text file

f = open("pyPollOut.txt","w")
f.write("Election Results\n")
f.write("-----------------------\n")
f.write("Total Votes: " + str(voteCount)  + "\n")
f.write("-----------------------\n")
# Loop through the tally and create the textfile
for candidate in voteTally:
    f.write(candidate + " " + "%5.2f"% ((voteTally[candidate]/voteCount)*100) + "% (" + str(voteTally[candidate]) + ")\n")
f.write("-----------------------\n")
f.write("Winner: " + winner + "\n")
f.write("-----------------------\n")
f.close()

