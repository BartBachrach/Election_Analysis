# Add our dependencies
import csv
import os

# Assign a variable for the file to load from a path
file_to_load = os.path.join('/Users/adambachrach/Desktop/data-bootcamp/Election_Analysis/Resources/election_results.csv') #ASK TUTOR ABOUT THE INDIRECT FILE PATH METHOD

#assign a variable to save the file to a path
file_to_save = os.path.join('/Users/adambachrach/Desktop/data-bootcamp/Election_Analysis/analysis/election_analysis.txt') #ASK TUTOR ABOUT THE INDIRECT FILE PATH

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []
candidate_votes = {}

# County Options
county_options = []
county_votes = {} 

# Track the winning candidate, vote count, and percentage
winning_candidate = ""


# Winning candidate and winning count tracker
winning_county = " "
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
                # To do: read and analyze the data here.
                file_reader = csv.reader(election_data)

                # Print the header row.
                headers = next(file_reader)
                
                # Print each row in the csv file.
                for row in file_reader: 
                    # add to the total vote
                    total_votes += 1
                    # Print the candidate name from each row
                    candidate_name = row[2] 

                    # extract the county name from each row
                    county_name = row[1]

                    # if the candidate does not match any existing names, add it to the list
                    if candidate_name not in candidate_options:
                        # add name to list if not already there
                        candidate_options.append(candidate_name)
                        # and begin tracking that candidates voter count
                        candidate_votes[candidate_name] = 0
                    # add a vote to that candidate's count
                    candidate_votes[candidate_name] += 1
                    
                    if county_name not in county_options:
                            
                        # Add the candidate name to the candidate list
                            county_options.append(county_name)
                            #begin tracking the candidates vote count
                            county_votes[county_name] = 0
                # Add a vote to that candidate's count
                    county_votes[county_name] += 1
                # Save the results to our text file.
                with open(file_to_save, "w") as txt_file:
                                    election_results = (
                                        f"\nElection Results\n"
                                        f"---------------------\n"
                                        f"Total Votes: {total_votes:,}\n"
                                        f"---------------------\n\n"
                                        f"(Candidate Votes:\n")
                                    
                                    print(election_results, end="")
                                    # Save the final vote count to the text file
                                    txt_file.write(election_results)
                                    for candidate_name in candidate_votes:
                                        #2 retrieve vote count of a candidate
                                                votes = candidate_votes[candidate_name]
                                            #3 calculate the percentage of votes
                                                vote_percentage = float(votes) / float(total_votes) * 100
                                        # print the candidate name and percentage of votes
                                                print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                                        # To do: print out each candidates name, vote count, and percentage of
                                        # votes to the terminal
                                        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")

                                        # Determine winning vote count and candidate
                                        # Determine if the votes is greate than the winning count
                                                if (votes > winning_count) and (vote_percentage > winning_percentage):
                                            # If true then set the winning_count = votes and winning_percent = 
                                            # vote_percentage
                                                    winning_count = votes

                                                # And, set the winning_candidate equal to the candidates name.
                                                    winning_candidate = candidate_name
                                                    winning_percentage = vote_percentage
                                    # Print the winning candidates' results to the terminal
                                    winning_candidate_summary = (
                                            
                                            f"-----------------------\n"
                                            f"Winner: {winning_candidate}\n"
                                            f"Winning Vote Count: {winning_count:,}\n"
                                            f"Winning Percentage: {winning_percentage:.1f}%\n"
                                            f"-----------------------\n")
                                            
                        # print(winning_candidate_summary)
                                    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                                    print(winning_candidate_summary)
                                    txt_file.write(winning_candidate_summary) # ASK TUTOR WHY IS RAYMON ANTHONY DOANE APPEARING TWICE?
                                  

                                # Determine the percentage of votes for each candidate by looping through the counts.
                                    #1 Iterate through the candidate list
                                    for county_name in county_votes:
                                        #2 retrieve vote count of a candidate
                                                votes = county_votes[county_name]
                                            #3 calculate the percentage of votes
                                                vote_percentage = float(votes) / float(total_votes) * 100
                                        # print the candidate name and percentage of votes
                                                print(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
                                        # To do: print out each candidates name, vote count, and percentage of
                                        # votes to the terminal
                                        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")

                                        # Determine winning vote count and candidate
                                        # Determine if the votes is greate than the winning count
                                                if (votes > winning_count) and (vote_percentage > winning_percentage):
                                            # If true then set the winning_count = votes and winning_percent = 
                                            # vote_percentage
                                                    winning_count = votes

                                                # And, set the winning_candidate equal to the candidates name.
                                                    winning_candidate = county_name
                                                    winning_percentage = vote_percentage
                                    # Print the winning candidates' results to the terminal
                                    winning_county_summary = (
                                            f"-----------------------\n"
                                            f"Winner: {winning_candidate}\n"
                                            f"Winning Vote Count: {winning_count:,}\n"
                                            f"Winning Percentage: {winning_percentage:.1f}%\n"
                                            f"-----------------------\n")
                        # print(winning_candidate_summary)
                                    county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
                                    print(winning_county_summary)
                                    txt_file.write(winning_county_summary) # ASK TUTOR WHY IS RAYMON ANTHONY DOANE APPEARING TWICE?
                                    election_data.close()               