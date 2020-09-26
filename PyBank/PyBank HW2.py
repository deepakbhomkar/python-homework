
# Import the pathlib and csv library
from pathlib import Path
import csv

print(f"Current Working Directory: {Path.cwd()}")

# Set the file path
csvpath = Path('budget_data.csv')

# Initialize [budget] - list of dictionaries
budget = []

# Open the input path as a file object for csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Go to the next row from the start of the file skip header for record processing
    header = next(csvreader)

    # Previous record profit & loss & row number of record being processed in for loop
    prev_pnl = 0
    row_number = 0
    
    # Iterate for each row after the header row is skipped
    for row in csvreader:
        # Initialize [pnl_month] dictionary for each record read
        pnl_month = {}
        
        # Populate dictionary pnl_month with csv records
        pnl_month["month"] = row[0]
        pnl_month["pnl"] = int(row[1])
        
        # Calculate increase or decrease using previous record's proft/loss.
        # First record will have increase decrease default set to 0.
        if row_number == 0:
            pnl_incr_decr = 0
        else:
            pnl_incr_decr = int(row[1]) - prev_pnl
        
        # Go to next row in csv file
        row_number += 1
        
        # Set previous P&l in variable and populate increase decrease value for each record
        prev_pnl = int(row[1])
        pnl_month["incr_decr"] = pnl_incr_decr
        
        # append dictionary {pnl_month} to list budget 
        budget.append(pnl_month)

# Initialize variables
index = 0
this_record_pnl = 0
this_record_incr_decr = 0
net_pnl = 0
total_months = 0
avg_incr_decr = 0
net_incr_decr = 0
net_months = 0
max_incr_profits = 0
max_decr_profits = 0

# Iterate list [budget]

while index < len(budget):
    
    # Sum up total number months
    total_months += 1
    
    # capture current record's P&L and Increase/Decrease in variable with Integer conversion
    this_record_pnl = int(budget[index]["pnl"])
    this_record_incr_decr = int(budget[index]["incr_decr"])
    
    # Sum up P&L and Increase/Decrease
    net_pnl = net_pnl + this_record_pnl
    net_incr_decr = net_incr_decr + this_record_incr_decr
    
    # Capture the greatest increase in profits with its month and the greatest decrese in profits with its month
    if this_record_incr_decr > max_incr_profits:
        max_incr_profits = this_record_incr_decr
        max_incr_month = budget[index]["month"]
    elif this_record_incr_decr < max_decr_profits:
        max_decr_profits = this_record_incr_decr
        max_decr_month = budget[index]["month"]
    
    # Go to next record
    index += 1

# Calculate average increase decrease - (sum of all increase decrease / number of months -1)
net_months = total_months - 1
avg_incr_decr = net_incr_decr/net_months

# Print the calculations

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_pnl}")
print(f"Average  Change: ${round(avg_incr_decr,2)}")
print(f"Greatest Increase in Profits: {max_incr_month} (${max_incr_profits})")
print(f"Greatest Decrease in Profits: {max_decr_month} (${max_decr_profits})")

# Set output file name
output_path = 'output.txt'

# Open the output path as a file object
with open(output_path, 'w') as file:
    # 
    file.write(f"Financial Analysis\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_pnl}\n")
    file.write(f"Average  Change: ${round(avg_incr_decr,2)}\n")
    file.write(f"Greatest Increase in Profits: {max_incr_month} (${max_incr_profits})\n")
    file.write(f"Greatest Decrease in Profits: {max_decr_month} (${max_decr_profits})\n")