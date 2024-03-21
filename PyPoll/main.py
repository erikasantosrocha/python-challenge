'''
PyPoll
'''

# Import the os module
import os

# Module for reading csv files
import csv

# Define the csv file
csv_path = os.path.join('Resources', 'election_data.csv')

# Read the csv module
with open(csv_path) as csv_file:

    # CSV reader specifies delimiter and variable that hold the content #csv reader variable
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the row header and ignore it as part of the data
    csv_header = next(csv_reader)

    # Define the variables and assign its initial value as zero
    total_votes = 0
    charles_votes = 0
    diana_votes = 0
    raymon_votes = 0

    # Iterate through the row in the file dataset
    for row in csv_reader:

        # At each iteration, the value of total_votes is increased by 1
        total_votes +=1

        # Every time the candidate's name is found, increment the candidate's votes by 1 and store it
        if row[2] == "Charles Casper Stockham": 
            charles_votes +=1
        elif row[2] == "Diana DeGette":
            diana_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes +=1

    # Calculate the percentage of votes each candidate won
    charles_percent = (charles_votes/total_votes) * 100
    diana_percent = (diana_votes/total_votes) * 100
    raymon_percent = (raymon_votes/total_votes) * 100

    # We create two lists to store the candidates and the number of votes for each of them
    candidate = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
    candidate_votes = [charles_votes, diana_votes, raymon_votes]
 
    # Create a dictionary with the two lists and zip them together 
    dict_cand_votes = dict(zip(candidate, candidate_votes))

    # Find the winner with the max votes by using the max function that returns the key in the dict
    key = max(dict_cand_votes, key = dict_cand_votes.get)

    # Print Summary of results
    print("Election Results")
    print("-----------------------------------")
    print(f"Total Votes: {(total_votes)}")
    print(f"-----------------------------------")
    print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
    print(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
    print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
    print(f"-----------------------------------")
    print(f"Winner: {key}")
    print(f"-----------------------------------")

# Export the results as text file
    export_file = os.path.join ("..", "PyPoll", "analysis", "Election_Results_Summary.txt")

    with open(export_file,"w") as file:
    
        # Write the results on Election_Results_Summary.txt file
        file.write("Election Results")
        file.write("\n")
        file.write("-----------------------------------")
        file.write(f"Total Votes: {(total_votes)}")
        file.write("\n")
        file.write(f"-----------------------------------")
        file.write("\n")
        file.write(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
        file.write("\n")
        file.write(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
        file.write("\n")
        file.write(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
        file.write("\n")
        file.write(f"-----------------------------------")
        file.write("\n")
        file.write(f"Winner: {key}")
        file.write("\n")
        file.write(f"-----------------------------------")