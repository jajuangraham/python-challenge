import os
import csv

# Path to the CSV file
budget_data = os.path.join('Resources', 'budget_data.csv')

# Variables to hold the analysis data
total_months = 0
total_profit_loss = 0
value = 0
change = 0
dates = []
profits = []
changes = []  # To track changes between months

# Read the CSV file
with open(budget_data, newline='') as budget_data_file:
    csvreader = csv.reader(budget_data_file, delimiter=",")
    
    # Read the header row
    csv_header = next(csvreader)
    
    # Read the first row (initialize variables)
    first_row = next(csvreader)
    total_months += 1
    total_profit_loss += int(first_row[1])
    value = int(first_row[1])
    dates.append(first_row[0])

    # calucalate rows
    for row in csvreader:
        # Update total months
        total_months += 1
        
        # Add to the total profit/loss
        total_profit_loss += int(row[1])
        
        # Calculate the change in profit/loss
        change = int(row[1]) - value
        changes.append(change)
        value = int(row[1])
        
        # Append the date and profit/loss 
        dates.append(row[0])
        profits.append(int(row[1]))
    
    # Calculate the greatest increase and decrease
    greatest_increase = max(changes)
    greatest_decrease = min(changes)
    greatest_increase_date = dates[changes.index(greatest_increase) + 1]
    greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]

# Print the results
print("Financial Analysis")
print("")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${round(sum(changes) / len(changes), 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
