# Election Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.10.4, Visual Studio Code, 1.67.2

## Summary
The analysis of the election show that:
- There were "x" votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette who received 73.8% of the vote and 272,892 number of votes.


# Election Audit
## Overview of Election Audit
The purpose of this Election audit is to determine the winning candidate of the election that took place, as well as the county that had the most votes in the election.

## Election-Audit Results
Following are the results obtained from the audit:
- The total number of votes cast in this election were 369,711.
- Breakdown of votes cast and percentage of total votes for each **County**:

![Breakdown of County Votes](https://github.com/msshahid21/election_analysis/blob/main/resources/CountyBreakdown.png)
- The county that had the largest number of votes was Denver.
- Breakdown of the number of votes and percentage of total votes for each **Candidate**:

![Breakdown of Candidate Votes](https://github.com/msshahid21/election_analysis/blob/main/resources/CandidateBreakdown.png)
- Given the above chart, it can be seen that Diana DeGette won the election with 73.8% of the total votes.

## Election-Audit Summary
In conclusion this script was able to help determine that the winner of this election was Diana DeGette with 73.8% of the total votes, and that Denver was the County that had cast the most votes.

This script could be used to analyze any election dataset as it gets all the unique candidates and counties from the dataset without any input from the user. Additionally, it automatically populates the analysis text file and computer terminal to provide the results of the election.

The following modifications can be made to make it even further usable for other elections:
- In the event that the script is to be used for other elections, such as for school elections, or presidential elections. The user could be prompted to enter a column in the dataset that they would like to group by to further analyse the data. For example, if they wanted to group by gender to see which gender voted the most in the election.

- Additionally, this script could also be modified to give weightings to different counties in the election. For example, in a presidential election each State gets a certain number of seats thus giving each state a different weighting in deciding the ultimate winner. So the user could pass a weighting dictionary, that could be used within the script to determine the election winner not just by popular vote but by number of seats won.