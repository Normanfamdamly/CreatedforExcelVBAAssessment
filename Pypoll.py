# The date we need to retrieve
import csv
import os
# Assign a variable for the file to load and the path
file_to_load =os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_Save = os.path.join("analysis", "election_analysis.txt")

# 1. The total number of votes cast
total_votes = 0

# Canidate Options and votes
candidate_options = []
# Declare empty dictionary
candidate_votes = {}

# Declare variable that holds an empty string value for the winning canidate.
winning_candidate = ""
# Declare the variable for teh "winning count."
winning_count = 0
# Declare the variable for the "winning_percentage" equal to zero
winning_percentage = 0

# Open election results and read the file
with open(file_to_load) as election_data:
    # To Do: read and analyze the data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read Print the header row.
    headers = next(file_reader) 

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. A complete list of canidates who receied votes     
        total_votes += 1

        # Print the canidiate name from each row
        candidate_name = row[2]

        # If the canidate does not any exisitng canidate . . .
        if candidate_name not in candidate_options:
            # Add the canidate name to the canidate list.
            candidate_options.append(candidate_name)  

            # 2. Begin tracking that canidates vote count.
            candidate_votes[candidate_name]= 0

         # Add a vote to the canidate's count.
        candidate_votes[candidate_name] += 1


    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # # Save the final vote count to the text file.
               
# Determine the percentage of votes for each canidate by looping through the counts.
# 1. Iterate throug the canidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of canidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
   
   # To do: print out each canidates name, vote count, and percentage of 
   # votes to the terminal
    candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")    
    print(candidate_results)
    

   # Determine winning vote count and canidate
   # Determine if the votes is great than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning_percentage = # vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_canidate equal to the canidate's name.
        winning_candidate = candidate_name

    # 3 Print the winning candidate, vote count and percentage to the terminal
    winning_candidate_summary = (
        f"---------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winner Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------\n")
    print(winning_candidate_summary)

# Close the file
    election_data.close()
# Print out the election data 




    
