# The date we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of canidates who receied votes
# 3. The percentage of votes each canidate won
# 4. The total number of votes wach canidate won
# 5. The winner of the election based on popular vote.
import csv
import os
# Assign a variable for the file to load and the path
file_to_load =os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_Save = os.path.join("analysis", "election_analysis.txt")

# Open election results and read the file
with open(file_to_load) as election_data:
    # To Do: read and analyze the data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read Print the header row.
    headers = next(file_reader)
    print(headers)

# Close the file
election_data.close()
# Print out the election data 

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the optn statement to open the file as a text file
with open(file_to_save, "w") as txt_file:
# Write some data to this file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
  

# Close the file
outfile.close()


    
