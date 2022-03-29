# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join('/Users/adambachrach/Desktop/data-bootcamp/Election_Analysis/netflix_ratings.csv')

# Specify the file to write to the movie data.
outfile = os.path.join('/Users/adambachrach/Desktop/data-bootcamp/Election_Analysis/supp_output.txt')

# Set a variable to false to check if we found the video
found = False

# Open the NetFlix CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == video:

            # Set the variable created in Step 1 to confirm we have found the video
            found = True
 
            # Open the file using "write" mode. Specify the variable to hold the contents
            with open(outfile, "w") as txt_file:
            
            # Create a variable to hold the title, rating level, and the movie rating inside parentheses.
                movie_data = (row[0], "", row[2], "", row[1])
            
            # Write the movie data to the text file.
                

            # Print the movie data to the console.
                print(movie_data)



        # Stop at first results to avoid duplicates
        break 

    # If the video is never found, alert the user
if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")
