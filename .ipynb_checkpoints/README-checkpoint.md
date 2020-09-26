# Python-Homework Week 2
# PyBank

This is Python script for analyzing the financial records of your company. You will be provided with a financial dataset in this file: budget_data.csv. This dataset is composed of two columns, Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting, so the records are simple.)
Your task is to create a Python script that analyzes the records to calculate each of the following:

The total number of months included in the dataset.

The net total amount of Profit/Losses over the entire period.
The average of the changes in Profit/Losses over the entire period.
The greatest increase in profits (date and amount) over the entire period.
The greatest decrease in losses (date and amount) over the entire period.

# Your resulting analysis should look similar to the following:

Financial Analysis

----------------------------
Total Months: 86

Total: $38382578

Average  Change: $-2315.12

Greatest Increase in Profits: Feb-2012 ($1926159)

Greatest Decrease in Profits: Sep-2013 ($-2196167)

# Output to txt file
Your final script should print the analysis to the terminal and export a text file with the results.

# (Optional)
# PyRamen

Welcome to Ichiban Ramen!
Opening a ramen shop has always been your dream, and now it's finally been realized––you're closing out on your second year of sales! Like last year, you need to analyze your business's financial performance by cross-referencing your sales data with your internal menu data to figure out revenues and costs for the year.
This year, you also want to analyze how well your business did on a per-product basis (as you have several choices of ramen) in order to better understand which products are doing well, which are doing poorly, and, ultimately, which products may need to be removed or changed.
You tried doing this type of per-product analysis last year in Excel, but you were not able to keep your reports up-to-date with your current sales data. Therefore, you need to innovate. With more customers and more data to process, you'll need a tool that will allow you to automate your calculations in a manner that scales with your business.
Enter Python! Python provides a wide range of capabilities for handling data, harnessing the power of low-level Python data structures and high-level development libraries, all the while supporting the automation and scalability needs for a growing enterprise.
In this homework assignment, you will need to:


## Read the Data
Complete the following:

Read in menu_data.csv and set its contents to a separate list object. (This way, you can cross-reference your menu data with your sales data as you read in your sales data in the coming steps.)

Initialize an empty menu list object to hold the contents of menu_data.csv.
Use a with statement and open the menu_data.csv by using its file path.
Use the reader function from the csv library to begin reading menu_data.csv.
Use the next function to skip the header (first row of the CSV).
Loop over the rest of the rows and append every row to the menu list object (the outcome will be a list of lists).
Set up the same process to read in sales_data.csv. However, instead append every row of the sales data to a new sales list object.

## Manipulate the Data
Write out the contents of the report dictionary to a text file. The report should output each ramen type as the keys and 01-count, 02-revenue, 03-cogs, and 04-profit metrics as the values for every ramen type as shown:

spicy miso ramen {'01-count': 9238, '02-revenue': 110856.0, '03-cogs': 46190.0, '04-profit': 64666.0}
tori paitan ramen {'01-count': 9156, '02-revenue': 119028.0, '03-cogs': 54936.0, '04-profit': 64092.0}
truffle butter ramen {'01-count': 8982, '02-revenue': 125748.0, '03-cogs': 62874.0, '04-profit': 62874.0}
tonkotsu ramen {'01-count': 9288, '02-revenue': 120744.0, '03-cogs': 55728.0, '04-profit': 65016.0}
vegetarian spicy miso {'01-count': 9216, '02-revenue': 110592.0, '03-cogs': 46080.0, '04-profit': 64512.0}
shio ramen {'01-count': 9180, '02-revenue': 100980.0, '03-cogs': 45900.0, '04-profit': 55080.0}
miso crab ramen {'01-count': 8890, '02-revenue': 106680.0, '03-cogs': 53340.0, '04-profit': 53340.0}
nagomi shoyu {'01-count': 9132, '02-revenue': 100452.0, '03-cogs': 45660.0, '04-profit': 54792.0}
soft-shell miso crab ramen {'01-count': 9130, '02-revenue': 127820.0, '03-cogs': 63910.0, '04-profit': 63910.0}
burnt garlic tonkotsu ramen {'01-count': 9070, '02-revenue': 126980.0, '03-cogs': 54420.0, '04-profit': 72560.0}
vegetarian curry + king trumpet mushroom ramen {'01-count': 8824, '02-revenue': 114712.0, '03-cogs': 61768.0, '04-profit': 52944.0}
