from calendar import c
import csv
from itertools import count
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")

# Assign a variable for the file to save and the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Initialize list of candidate names
candidate_options = []

# Initialize list of counties
county_list = []

# Initialize candidate votes dictionary
candidate_votes = {}

# Initialize county votes dictionary
county_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Highest vote county and vote count tracker
highest_county = ""
highest_vote_county = 0
highest_percentage_county = 0


# Open the election_results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row of the election_results file
    for row in file_reader:
        total_votes += 1

        # Add candidate name to candidate options
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Initialize each candidate to 0 votes
            candidate_votes[candidate_name] = 0
            candidate_options.append(candidate_name)

        # Add a vote to the candidates count
        candidate_votes[candidate_name] += 1

        # Add county name to county list
        county_name = row[1]

        if county_name not in county_list:
            # Initialize each county to 0 votes
            county_votes[county_name] = 0
            county_list.append(county_name)
        
        # Add a cote to the county votes
        county_votes[county_name] += 1

# Get Winning Candidate and Largest County Turnout
## Winning Candidate
for candidate in candidate_options:
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(total_votes)  * 100
    
    # Determine winning vote, count, and percentage
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate

## Largest County Turnout
for county in county_list:
    votes = county_votes[county]
    vote_percentage = float(county_votes[county]) / float(total_votes) * 100

    # Determine highest vote, count, and percentage
    if (votes > highest_vote_county) and (vote_percentage > highest_percentage_county):
        highest_county = county
        highest_vote_county = votes
        highest_percentage_county = vote_percentage


# Total Votes Header
election_results = (
    f"\nElection Results\n"
    f"---------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"---------------------------\n"
)

# Summary for Winning Candidate
winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------------\n"
)

# Summary for Largest County Turnout
highest_county_summary = (
    f"\n---------------------------\n"
    f"Largest County Turnout: {highest_county}\n"
    f"---------------------------\n"
)

# Print Header Row for Total Vote to the command line
print(election_results)

# Print County Results to the command line
print("County Votes:")
for county_name in county_list:
    
    # Calculate County Percentage of Total Votes
    county_percentage = float(county_votes[county_name]) / float(total_votes) * 100

    # Print Summary of each county to command line
    print(f"{county_name}: {county_percentage:0.1f}% ({county_votes[county_name]:,})")

# Print Largest County Turnout Summary
print(highest_county_summary)

# Print Candidate Results
for candidate in candidate_options:
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(total_votes)  * 100
    
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

# Print Winning Candidate Summary
print(winning_candidate_summary)

# Open election_analysis file for writing
with open(file_to_save, "w") as outfile:
    
    outfile.write(election_results)

    # Iterate through candidate options to get percentage of total votes
    for candidate in candidate_options:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes)  * 100
        
        # Determine winning vote, count, and percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

        # Print each candidates vote count and vote percentage
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        outfile.write(candidate_results)

    winning_candidate_summary = (
        f"----------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------------"
    )

    outfile.write(winning_candidate_summary)