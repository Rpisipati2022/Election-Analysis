# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join("Desktop","BOOTCAMP FILES","MODULE 3","Resources","election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("Desktop","BOOTCAMP FILES","MODULE 3","Election Analysis", "analysis","election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# County Options and county votes(to get votes by county)
county_options = []
county_votes = {}

# Initialize candidate measurement variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

#Read the file objects with the reader function. NOTE: This line is indented from the "with" statement above; if not 
#indented, Python closes the election_data file!!

    file_reader = csv.reader(election_data)
    
    #Read and print header row
    headers = next(file_reader)
    #For each row in the CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes +=1

    #Print the county name for each row
        county_name = row[1]
       
# 1: Create a county list and county votes dictionary.
 #If the county does not match any existing county. 
        if county_name not in county_options:
            
            #Add the county name to the county list
            county_options.append(county_name)
        #2. Begin tracking that county's vote count
            county_votes[county_name] = 0
            #Add a vote to that county's count
        county_votes[county_name] += 1
    # Verify that the program is doing what you intended
    print(county_votes)


# Track the winning candidate, vote count and percentage
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
    total_votes = 0

#Re-load the file, as the previous "print(county_votes)" was the last instruction and the "with" function closed the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read and print the header row
    headers = next(file_reader)

    #Print each row in the csv file:
    for row in file_reader:
        total_votes += 1
        #Get the candidate name for each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
        #2. Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
            #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    
    print(candidate_votes)

# Find the candidate that won the election
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        votes_percentage = float(votes)/float(total_votes) * 100
        
        candidate_results = (
            f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

 #Determine winning vote count and candidate
        #1. Determine of the votes are greater than the winning count
        if (votes>winning_count) and (votes_percentage> winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = votes_percentage
                    
                #Create a filename variable to a direct or indirect path to the file
                # Create a file to write the output to
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n")
    print(winning_candidate_summary)


# 2: Track the largest county and county voter turnout.
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
    total_votes = 0

# Read the csv and convert it into a list of dictionaries
total_votes = 0
county2_options = []
county2_votes = {}
with open(file_to_load) as election_data:

#Read the file objects with the reader function. NOTE: This line is indented from the "with" statement above; if not indented, Python closes the election_data file!!
    file_reader = csv.reader(election_data)
    
    #Read and print header row
    headers = next(file_reader)

    for row in file_reader:
        total_votes +=1

    #Extract the county name for each row
        county2_name = row[1]  
    # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county2_name not in county2_options:
            
            #Add the county name to the county list
            county2_options.append(county2_name)
        #2. Begin tracking that county's vote count
            county2_votes[county2_name] = 0
        
            #Add a vote to that county's count
        county2_votes[county2_name] += 1
            
    print(county2_votes)
    #print(total_votes)

    for county2_name in county2_votes:
        votes = county2_votes[county2_name]
        votes_percentage = float(votes)/float(total_votes) * 100
        
        county2_results = (
            f"{county2_name}: {votes_percentage:.1f}% ({votes:,})\n")
        print(county2_results)
        if(votes>winning_count) and (votes_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = county2_name
            winning_percentage = votes_percentage

        largest_county_summary = (
        f"------------------------\n"
        f"Largest County: {winning_candidate}\n"
        f"Largest Turnout: {winning_count:,}\n"
        f"Largest Percentage: {winning_percentage:.1f}\n")
    
           # 7: Print the county with the largest turnout to the terminal.
    print(largest_county_summary)


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        votes_percentage = float(votes)/float(total_votes) * 100
        
        # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {votes_percentage:.1f}% ({votes:,})\n")
       
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
    
         # 6f: Write an if statement to determine the winning county and get its vote count.


     # 8: Save the county with the largest turnout to a text file.


    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)


    # Save the winning candidate's name to the text file
    
