# Install Modules
import os
import csv
from pathlib import Path

# Setup path to read csv file
csvpath = Path("budget_data.csv")

# Set up variables
monthCount = 0
plPreviousMonth = 0
plChange = 0
plChangeSum = 0
greatestIncreaseDate = ""
greatestDecreaseDate = ""
greatestIncreaseAmt = 0
greatestDecreaseAmt = 0
plNet = 0
plChangeAverage = 0

# Open csv file
with open (csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

# Read the header row
    csv_header = next(csvreader)

# Loop through file
    for row in csvreader:

# Increment counter
        monthCount = monthCount+1

# Add new amount to sum
        plNet = plNet + int(row[1])

# set profit/loss change after the first month
        if(monthCount>1):
            plChange = int(row[1]) - plPreviousMonth

# Set "previous month P&L" to current month for next pass
        plPreviousMonth = int(row[1])

# Add current PL chagne to change sum
        plChangeSum = plChangeSum + plChange

# Check to see if greatest increase
        if(plChange>greatestIncreaseAmt):
            greatestIncreaseAmt = plChange
            greatestIncreaseDate = row[0]

# Check to see if greatest decrease
        if(plChange<greatestDecreaseAmt):
            greatestDecreaseAmt = plChange
            greatestDecreaseDate = row[0]

# After loop, calculate average
    plChangeAverage = plChangeSum / (monthCount -1)


# print out stats
    print("Financial Analysis")
    print("--------------------------------------------------")
    print("Total Months: " + str(monthCount))
    print("Total: $" + str(plNet))
    print("Average Change: $" + str(plChangeAverage))
    print("Greatest Increase in Profits: " + greatestIncreaseDate + " ($" + str(greatestIncreaseAmt) + ")")
    print("Greatest Decrease in Profits: " + greatestDecreaseDate + " ($" + str(greatestDecreaseAmt) + ")")

# Write stats to output file
f = open("pyBankOut.txt","w")
f.write("Financial Analysis\n")
f.write("--------------------------------------------------\n")
f.write("Total Months: " + str(monthCount) + "\n")
f.write("Total: $" + str(plNet) + "\n")
f.write("Average Change: $" + str(plChangeAverage) + "\n")
f.write("Greatest Increase in Profits: " + greatestIncreaseDate + " ($" + str(greatestIncreaseAmt) + ")\n")
f.write("Greatest Decrease in Profits: " + greatestDecreaseDate + " ($" + str(greatestDecreaseAmt) + ")\n")
f.close()