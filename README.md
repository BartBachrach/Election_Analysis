# Election Analysis
## Overview
In this analysis, we received election data in .csv format with 3 columns containing the Ballot ID, County Name, and Candidate Name, with each row representing a vote cast for the given candidate. From this data we can immediately determine the winning candidate and the total number of votes cast in the election. Digging deeper, we can also read into the data to give us the level of voter turnout in this election,  the county that voted most in favor of the winning candidate, and the county with the highest percentage of voters that went to the polls. The election commission wanted a breakdown of who won the election, how many votes they received, and what percentage, as well as voter turnout by county and percentage of votes won in each county. 

## Method
This analysis required us to read through the data set and determine how many votes were cast for each candidate and from each county. We set our code to establish an empty list of candidate options and county options, and as it read through the file, add to the vote count for each. The result was an output of total votes and the percentage of votes cast for each candidate and county. The election commission previously asked us to provide a similar breakdown of the candidates’ results, and from that we added to the code to also produce the results according to county name instead of candidate name. 

## Results
We determined that Dianna DeGette was the winner of the election with 73.8% of the votes cast for her, a landslide victory, followed by Charles Casper Stockham with 23.0% of the votes, and Raymon Anthony Doane with the remaining 3.1%. 
Denver county voters turned out in the greatest numbers at 306,055 total votes cast, the majority of which were in favor of DeGette, followed by Jefferson and Arapahoe counties. One explanation for this is that Denver county is the most populous of the 3 counties that comprise the Denver area, although other factors may affect this analysis such as access to polls and means of transportation TO the polls. 
![This is an image][Module_3_Challenge_Screenshot.png]
