import os
import csv
poll_csv = os.path.join('election_data.csv')
with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    votes = 0
    total = 0
    candidate_list = [] 
    khan = 0
    correy = 0
    li = 0
    otooley = 0
 
    for row in csvreader:
        votes += 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        if row[2] == "Khan":
            khan += 1  
        if row[2] == "Correy":
            correy += 1 
        if row[2] == "Li":
            li += 1 
        if row[2] == "O'Tooley":
            otooley += 1 
    perc_khan = int((khan/votes)*100)
    perc_correy = int((correy/votes)*100)
    perc_li = int((li/votes)*100)
    perc_otooley = int((otooley/votes)*100)


      
    # traverse for all elements 
    # for x in list1: 
    #     # check if exists in unique_list or not 
    #     if x not in unique_list: 
    #         unique_list.append(x) 


    output_path = os.path.join("PyPoll.txt")
    with open(output_path, 'w', newline='') as textfile: 
        print(" ", file=textfile)
        print("Election Results", file=textfile)
        print("-------------------------", file=textfile)
        print("Total Votes: " + str(votes), file=textfile)
        print("-------------------------", file=textfile)
        print(candidate_list[0] + ": " + str(perc_khan) + "% (" + str(khan) + ")", file=textfile)
        print(candidate_list[1] + ": " + str(perc_correy) + "% (" + str(correy) + ")", file=textfile)
        print(candidate_list[2] + ": " + str(perc_li) + "% (" + str(li) + ")", file=textfile)
        print(candidate_list[3] + ": " + str(perc_otooley) + "% (" + str(otooley) + ")", file=textfile)

# Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
