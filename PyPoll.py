# Add our dependencies
import csv
import os

# Assign a variable for the file to load from a path
file_to_load = os.path.join('/Users/adambachrach/Desktop/Election_Analysis/Resources/election_results.csv')

#assign a variable to save the file to a path
file_to_save = os.path.join('/Users/adambachrach/Desktop/Election_Analysis/analysis/election_analysis.txt')

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print the heade row.
    headers = next(file_reader)
    print(headers)

    
    election_data.close()   