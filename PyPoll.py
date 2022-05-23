import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")

# Assign a variable for the file to save and the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Initialize list of candidate names
candidate_options = []

# Initialize votes dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

# Open election_analysis file for writing
with open(file_to_save, "w") as outfile:
    
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n"
    )
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