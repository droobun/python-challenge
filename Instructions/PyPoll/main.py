# PyPoll main
from operator import index
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print("CSV Header: " + str(csv_header))

# The total number of votes cast
# A complete list of candidates who received votes
    vote_total = 0
    candidates = []
    candidate_votes = [0,0,0]

    for row in csvreader:
        vote_total = vote_total + 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidates.index(candidate)] += 1
        else:
            candidate_votes[candidates.index(candidate)] += 1
    

# The percentage of votes each candidate won
    # for candidate in candidates:
    #     f.write(candidates.index(candidate))
# The total number of votes each candidate won
with open('analysis/PyPoll_Analysis.txt', 'w') as f:
# The winner of the election based on popular vote.
    f.write("Election Results\n")
    f.write("-------------------------------\n")
    f.write("Total Votes: " + str(vote_total) + "\n")
    f.write("-------------------------------\n")
# for each in candidates:
#     f.write(each)
# for votes in candidate_votes:
#     f.write(votes)
    for vote_index in range(len(candidates)):
        vote_count = (candidate_votes[vote_index])
        candidate_name = str(candidates[vote_index])
        vote_percentage = float(vote_count)/vote_total *100
    
        f.write(candidate_name + ": "  + str(round(vote_percentage,3)) +  "% (" + str(vote_count) + ")\n")

    winner = candidate_votes.index(max(candidate_votes))
    f.write("-------------------------------\n")
    f.write("Winner: " + candidates[winner] + "\n")
    f.write("-------------------------------\n")