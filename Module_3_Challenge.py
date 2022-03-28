# import necessary dependencies
import csv
import os

# set the data file we need to open first
data_file = os.path.join('/Users/adambachrach/Desktop/data-bootcamp/Election_Analysis/Resources/election_results.csv')
# set the output file where the results go next
output_file = os.path.join('/Users/adambachrach/Desktop/data-bootcamp/Election_Analysis/Practice_Output_File.txt')

# initialize the voter turnout variable to 0
total_voters = 0

#create an empty dictionary of counties
counties = []

# set an empty dictionary for votes by county
county_votes= {}

# establish the 3 outputs
Highest_County = " "
county_turnout = 0
county_percent = 0


# open the data file to read and assign it a name for this code sequence
with open(data_file) as election_data:
    
    # get the python file reader to start reading the data file
    file_reader = csv.reader(election_data)
    
    # print the header row
    headers = next(file_reader)

    # print each row in the data file
    for row in election_data:
        
        # increase the voter turnout by 1
        total_voters += 1

        # print the county name from row 1
        county_name = row[1]

        # in case we find a name we didn't expect
        if county_name not in counties:
            
            # if county name not in the dict, add it
            counties.append(county_name)

    # begin county votes according to their values in column 1
    total_voters[county_name] += 1
    # save the results to our text file
    with open(output_file, "w") as txt_file
