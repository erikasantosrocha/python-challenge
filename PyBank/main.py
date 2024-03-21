'''
PyBank
'''
# Import the os module
import os

# Module for reading csv files
import csv

# Define the csv file
csv_path = os.path.join('Resources', 'budget_data.csv')

# Read the csv module
with open(csv_path) as csv_file:

    # CSV reader specifies delimiter and variable that hold the content #csv reader variable
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the row header and ignore it as part of the data
    csv_header = next(csv_reader)

    # Define empty lists for the variables to iterate through specific rows
    total_month = []
    total_profit = []
    
    # Iterate through the row in the file dataset
    for row in csv_reader:

        # Append the total months and total profit/losses to the lists
        total_month.append(row[0])
        total_profit.append(int(row[1]))

    # Define empty list for the monthly_change variable for profit/losses over the entire period
    monthly_change = []
    
    # Iterate through the profit/losses to get the monthly change
    for i in range(len(total_profit)-1):

        # Calculate the profit/losses change between two consecutive months and append it to monthly_change
        monthly_change.append(total_profit[i+1]-total_profit[i])

    # Obtain the max and min profit of the monthly change list
    max_increase_profit = max(monthly_change)
    max_decrease_profit = min(monthly_change)

    # Associate the max and min profit/loss to the month list and the index
    # By adding 1 to the index, we get the next month in the list, which is associated with the monthly change
    max_increase_month = monthly_change.index(max(monthly_change)) + 1
    max_decrease_month = monthly_change.index(min(monthly_change)) + 1

    # Print Summary of results
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {len(total_month)}")
    print(f"Total: ${sum(total_profit)}")
    print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
    print(f"Greatest Increase in Profits: {total_month[max_increase_month]} (${(str(max_increase_profit))})")
    print(f"Greatest Decrease in Profits: {total_month[max_decrease_month]} (${(str(max_decrease_profit))})")

    # Export the results as text file
    export_file = os.path.join ("..", "PyBank", "analysis", "Financial_Analysis_Summary.txt")

    with open(export_file,"w") as file:
    
        # Write the results on Financial_Analysis_Summary.txt file
        file.write("Financial Analysis")
        file.write("\n")
        file.write("-----------------------------------")
        file.write("\n")
        file.write(f"Total Months: {len(total_month)}")
        file.write("\n")
        file.write(f"Total: ${sum(total_profit)}")
        file.write("\n")
        file.write(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
        file.write("\n")
        file.write(f"Greatest Increase in Profits: {total_month[max_increase_month]} (${(str(max_increase_profit))})")
        file.write("\n")
        file.write(f"Greatest Decrease in Profits: {total_month[max_decrease_month]} (${(str(max_decrease_profit))})")