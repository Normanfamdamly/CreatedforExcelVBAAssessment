# Election Analysis

## Project Overview
A Colorado Board of Elections has asked that I complete the election audit of the recent congressional election, looking at data from paper-ballots, machines-ballots and mail-in ballots. The election data was provided in an electronic format for review.

My analysis consisted of looking at the following seven items:

    1. Calculate the total number votes cast and voter turnout for each county.
    2. Gather a complete list of the candidates who received votes.
    3. Calculate the total number of votes each candidate received.
    4. Calculate the percentage of votes each candidate recevied.
    5. Calculate the percentage of votes for each county out of the total count.
    6. Determine the county with the highest voter turnout.
    7. Determine the winner of the election based on the popular vote.

## Resources
- Election_Results.CSV is our data source
- Python 3.6.7, Visual Studio are the systems we are utilizing

## Summary
The analysis of the elctions shows that:


    Election Results
    -------------------------
    Total Votes: 369,711
    -------------------------

    County Votes:
    Jefferson: 10.5% (38,855)
    Denver: 82.8% (306,055)
    Arapahoe: 6.7% (24,801)
    --------------------------
    Largest County Turnout Denver
    --------------------------
    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
    -------------------------
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    -------------------------

There was a large voter turn-out in Denver County which would be surpising considering the urban nature of the county. But considering the large rual population in Arapahoe and Jefferson County and I can understand the large discrepancy in turnout.  The winner of the congressional seat was Diana DeGette with 73.8% of the popular vote.

## Election Audit Summary
The program has been written to allow for use in any other congressional race through out Cololrado.  All the main loops for the data, are maintained in a general format and can be plug and play for any district.  All that will need to be upated is the report name you are pulling the data from, as shown below.

        # Add a variable to load a file from a path.
        file_to_load = os.path.join("Resources", "election_results.csv")
        # Add a variable to save the file to a path.
        file_to_save = os.path.join("analysis", "election_analysis.txt")

If you wanted to use this for the Presidental Election, you could as well and there would not need to be any alterations at all. The code written for the candidate and county calcutions would work for Presidental candidates, all that would require up would be the file name you are loading the data from, plus the amount of time it would take to run. This would take longer due to the higher numbe of voters that historically turn out for Presidental elections.


## Challenge Overview
The challenges faced were technical at times.  Getting VS Code to find our file was a bit of a challenge, but with the help of Google and our TA, we were able to termine it was a setting issue and not a coding issue.  One the setting was corrected in VS code we were good to go. Then from there the difficulty resulted from not knowing for sure where to place the code so it would provide me a full analysis. The placement of the f-string and the print request location could change whether you received 1 candidate or all.


