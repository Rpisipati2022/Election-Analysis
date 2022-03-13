# OVERVIEW OF ELECTION AUDIT
The purpose of the current analysis is to examine total votes cast in the congressional elections in three Colorado counties and determine which candidate won the popular vote. While doing this we also want to determine which of these three counties had the largest voter turnout.

## Election-Audit Results:
-	Total votes cast in the congressional election in these three counties were 369,711
-	Results by county:
o	Arapaho county:	24,801 votes (6.7% of total votes cast)
o	Denver county:	306,055 votes (82.8% of total votes cast)
o	Jefferson county:	38,855 votes (10.5% of total votes cast)
-	Denver county had the largest voter turnout at 306,055 votes cast
-	Votes received by the three candidates are:
o	Charles Casper Stockham	85,213 (23.0%)
o	Diana DeGette			272,892 (73.8%)
o	Raymond Anthony Doane	11,606 (3.1%)
-	Winner of the election based on total popular vote count was Diana DeGette (272,892 votes, 73.8% of total votes cast)

## Election-Audit Summary:
The data analyzed in this election was limited to three candidates competing in three counties. This script successfully analyzed the data and was able to determine the overall winner as well as details by county. This script can also be used to analyze larger elections: more counties and more candidates. Modifications to be made to look at additional counties and additional candidates would include

### A) Approach to the Analysis:
-	Analysis of each county in detail, to determine percent voter turnout in that county. This analysis would provide additional insight into the political sensitivities of each county and key issues of interest to the voting population in that county – are there topics important enough to bring out the vote?
-	Individual analysis of each candidate to see how they did in each county. E.g. in this election, while Diane DeGette was the overall winner with 73.8% of the total vote, she actually lost in Jefferson county:

### ARAPAHO	Votes		6.7%
Charles Casper Stockham	8,302 (33.5%)
Diana DeGette	15,647  (63.1%)
Raymon Anthony Doane	852	 (3.4%)
Total	24,801		
			
### DENVER	Votes		82.8%
Charles Casper Stockham	57,188  (18.7%)
Diana DeGette	239,282. (78.2%)
Raymon Anthony Doane	9,585		(3.1%)
Total	306,055		
			
### JEFFERSON	Votes		10.5%
Charles Casper Stockham	19,723		(50.8%)
Diana DeGette	17,963		(46.2%)
Raymon Anthony Doane	1,169		(3.0%)
Total	38,855		
			
Total Votes	369,711		


### B) Data completeness:
The current data only shows Voter ID, county and candidate the person voted for. It is unclear whether this is a primary election, i.e. limited to voter’s registered party in most states, or a general election where everyone can vote. 

Benefits of this proposed approach include:
-	One script to analyze any number of county/candidate combinations
-	The original data file election_results.csv is not changed so the original data remains intact no matter how the analysis is conducted
-	Additional analyses are possible as more data types are included in the original data set, e.g. voters’ registered political party, specific ballot issues, etc.
