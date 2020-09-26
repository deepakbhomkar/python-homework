# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries

import csv
from pathlib import Path

# Set file paths for menu_data.csv and sales_data.csv

menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# Initialize list objects to hold our menu and sales data

menu = []
sales = []

# Read in the menu data into the menu list

with open(menu_filepath, 'r') as csvmenufile:
    csvmenureader = csv.reader(csvmenufile, delimiter=',')
    
    header = next(csvmenureader)
    
    for item, category, description, price, cost in csvmenureader:
        
        # Individual list
        menu_row = []
        
        # Append to individual list
        menu_row.append(item)
        menu_row.append(category)
        menu_row.append(description)
        menu_row.append(price)
        menu_row.append(cost)
        
        # Append individual list to menu list
        menu.append(menu_row)

print(menu)


# Read in the sales data into the sales list

with open(sales_filepath, 'r') as csvsalesfile:
    csvsalesreader = csv.reader(csvsalesfile, delimiter=',')
    
    header = next(csvsalesreader)
    
    for line_item_id, date, credit_card_num, quantity, menu_item in csvsalesreader:
        
        # Individual list sales_row[]
        sales_row = []
        
        # Append to individual list sales_row[]
        sales_row.append(line_item_id)
        sales_row.append(date)
        sales_row.append(credit_card_num)
        sales_row.append(quantity)
        sales_row.append(menu_item)
        
        # Append individual list to menu list
        sales.append(sales_row)

# Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
sales_row_count = 0
quantity = 0
price = 0
cost = 0
profit = 0
sales_item = ""
sales_item_exist = ""

# Loop over every row in the sales list object

for line_item_id, date, credit_card_num, quantity, menu_item in sales:
    
    # Set quantity and sales_item
    quantity = int(sales[sales_row_count][3])
    sales_item = sales[sales_row_count][4]
    
    # If the item value not in the report, add it as a new entry with initialized metrics
    if sales_item in report:
        sales_item_exist = True
    else:
        report[sales_item] = {"01-count": 0, 
                              "02-revenue": 0, 
                              "03-cogs": 0, 
                              "04-profit": 0,}
    
    menu_row_count = 0
    
    # For every row in sales data, loop over the menu records to determine a match 
    for item, category, description, price, cost in menu:
        
        # set item, price and cost from menu 
        item = menu[menu_row_count][0]
        price = float(menu[menu_row_count][3])
        cost = float(menu[menu_row_count][4])
        
        # calculate count, revenue, cogs and profit for each sales_item
        profit = 0
        
        if sales_item == item:
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            profit = price - cost 
            report[sales_item]["04-profit"] += profit * quantity
        #else:
        #    print(f"{sales_item} does not equal {item}! NO MATCH!")
        
        # Go to next menu item
        menu_row_count += 1
    
    # Go to next record, increment row_count
    sales_row_count += 1

print(f"Total number of records in sales data: {sales_row_count}\n")

for key, value in report.items():
    print(key, value )


# Write out report to a text file
output_path = 'PyRamenoutput.txt'

# Open the output path as a file object
with open(output_path, 'w') as file:
    for key, value in report.items():
        #value = report[sales_item]
        file.write(str(key))
        file.write(' ')
        file.write(str(value))
        file.write("\n")

file.close()