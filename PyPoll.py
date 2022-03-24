# Add our dependencies
import csv
import os

# Assign a variable for the file to load from a path
file_to_load = os.path.join('/Users/adambachrach/Desktop/Election_Analysis/Resources/election_results.csv')

#assign a variable to save the file to a path
file_to_save = os.path.join('/Users/adambachrach/Desktop/Election_Analysis/analysis/election_analysis.txt')

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Declare an empty dictionary
candidate_votes = {} 

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print the heade row.
    headers = next(file_reader)
    
    # Print each row in the csv file.
    for row in file_reader:
        # add to the total vote
        total_votes += 1
# Print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            
        # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate by looping through the counts.
    #1 Iterate through the candidate list
    for candidate_name in candidate_votes:
        #2 retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3 calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
    # print the candidate name and percentage of votes

         # To do: print out each candidates name, vote count, and percentage of
         # votes to the terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greate than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set the winning_count = votes and winning_percent = 
            # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidates name.
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")
    print(winning_candidate_summary)
    

         # To do: print out each candidates name, vote count, and percentage of
         # votes to the terminal

    
election_data.close()   