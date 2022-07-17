# The date we need to retrieve
import csv
import os
# Assign a variable for the file to load and the path
file_to_load =os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_Save = os.path.join("analysis", "election_analysis.txt")

# 1. The total number of votes cast
total_votes = 0

# Canidate Options
canidate_options = []

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
        canidate_name = row[2]

        # If the canidate does not any exisitng canidate . . .
        if canidate_name not in canidate_options:
            # Add the canidate name to the canidate list.
            canidate_options.append(canidate_name)   

# 3a Print the total votes
print(canidate_options)





# 3b. The percentage of votes each canidate won
# 4. The total number of votes wach canidate won
# 5. The winner of the election based on popular vote.  
   

# Close the file
election_data.close()
# Print out the election data 




    
