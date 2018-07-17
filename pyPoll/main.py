import csv
path="Resources/election_data.csv"

#Create list of candidates
with open(path) as poll:
    next(poll)
    voteList=[]
    for row in csv.reader(poll):   
        candidate=str(row[2])
        voteList.append(candidate)


# The total number of votes cast
totalVotes=len(voteList)
khanVotes=voteList.count("Khan")
correyVotes=voteList.count("Correy")
liVotes=voteList.count("Li")
otooleyVotes=voteList.count("O'Tooley")

candidates=["Khan","Correy","Li","O'Tooley"]
candidateVotes=[khanVotes,correyVotes,liVotes,otooleyVotes]
winningTotal=(max(candidateVotes))
winningTotalLocation=(candidateVotes.index(winningTotal))
winner=candidates[winningTotalLocation]


print(" ")
print("Election Results")
print("----------------------------------------------------")
print("Total Votes: "+str(totalVotes))
print("----------------------------------------------------")
print("Khan: "+str(round((khanVotes/totalVotes)*100))+"% (Count: "+str(khanVotes)+")")
print("Correy: "+str(round((correyVotes/totalVotes)*100))+"% (Count: "+str(correyVotes)+")")
print("Li: "+str(round((liVotes/totalVotes)*100))+"% (Count: "+str(liVotes)+")")
print("O'Tooley: "+str(round((otooleyVotes/totalVotes)*100))+"% (Count:"+str(otooleyVotes)+")")
print("----------------------------------------------------")
print("Winner: "+str(winner))
print("----------------------------------------------------")

file = open("pyPoll.txt","w") 
file.write(" \n")

file.write(" ")
file.write("Election Results\n")
file.write("----------------------------------------------------\n")
file.write("Total Votes: "+str(totalVotes)+"\n")
file.write("----------------------------------------------------\n")
file.write("Khan: "+str(round((khanVotes/totalVotes)*100))+"% (Count: "+str(khanVotes)+")\n")
file.write("Correy: "+str(round((correyVotes/totalVotes)*100))+"% (Count: "+str(correyVotes)+")\n")
file.write("Li: "+str(round((liVotes/totalVotes)*100))+"% (Count: "+str(liVotes)+")\n")
file.write("O'Tooley: "+str(round((otooleyVotes/totalVotes)*100))+"% (Count:"+str(otooleyVotes)+")\n")
file.write("----------------------------------------------------\n")
file.write("Winner: "+str(winner)+"\n")
file.write("----------------------------------------------------")



# A complete list of candidates who received votes
# unique values in candidate column (2)

# The percentage of votes each candidate won
# The total number of votes each candidate won
#sum votes column (0) for each candidate
#divide votes for each candidate by total votes calc'd in previous step

#file.write each candidates' name with the percent of votes won and total votes won in parens

# The winner of the election based on popular vote.
#file.write winner and name of candidate with the most votes


# As an example, your analysis should look similar to the one below:

 # ```text
 # Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------
  #```