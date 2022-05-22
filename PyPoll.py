import csv
import os

# The data that needs to be retrieved:
# Assign a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")

# Open the election_results and read the file
with open(file_to_load, 'r') as election_data:
    # Print the file object
    print(election_data)


# Assign a variable for the file to save and the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open election_analysis file for writing
with open(file_to_save, "w") as outfile:
    
    # Title for election_analysis file
    outfile.write("Counties in the Election\n")
    outfile.write("_________________________\n")

    # Write three counties to the file
    outfile.write("Arapahoe\nDenver\nJefferson")


# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote