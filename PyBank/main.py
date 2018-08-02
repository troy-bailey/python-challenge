# Install Modules
import os
import csv
from pathlib import Path

# Setup path to read csv file
csvpath = Path("budget_data.csv")
print(csvpath)

# Set up variables
monthCount = 0
greatestIncreaseDate = ""
greatestDecreaseDate = ""
greatestIncreaseAmt = 0.0
greatestDecreaseAmt = 0.0
plNet = 0.0
plAvg = 0.0
print("variables Set")

# Open csv file

# Loop through file
# Increment counter
# Add new amount to sum
# Calculate profit/loss
# Check to see if greatest increase
# Check to see if greatest decrease
# After loop, print out stats
# Write stats to output file