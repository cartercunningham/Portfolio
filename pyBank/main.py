# Import modules - assumed couldn't use pandas module
import csv

# Import file and save as variable
path="Resources/budget_data.csv"

print(" ")
print("Financial Analysis")
print("-----------------------------------------------")

with open(path,newline="") as bank:
    bank = csv.reader(bank, delimiter=",")
    csv_header = next(bank)
    num_lines = 0
    
# The total number of months included in the dataset - iterate through rows until reaching the end
    for line in bank:
        num_lines += 1
    print("Number of Months: "+str(num_lines))

# The total net amount of "Profit/Losses" over the entire period

with open(path) as bank:
    headerline = next(bank)
    total = 0
    for row in csv.reader(bank):
        total += int(row[1])

    print("Net Profit/Loss for Period: $"+str(total))

# The average change in "Profit/Losses" between months over the entire period
# Take the difference between the previous month and the current month, append to a new list, take the average

with open(path) as bank:
    headerline = next(bank)

    revList=[]
    for row in csv.reader(bank):   
        thisMonth=int(row[1])
        revList.append(thisMonth)

revChange=[]
i=0

while i<40:
    diff=revList[i+1]-revList[i]
    revChange.append(diff)
    i+=1

avgChange=str(sum(revChange)/float(len(revChange)))
print("The average monthly change was: $"+avgChange)

# The greatest increase in profits (date and amount) over the entire period

with open(path) as bank:
    headerline = next(bank)

    monthList=[]
    for row in csv.reader(bank):
        thisMonth=row[0]
        monthList.append(thisMonth)

maxRevChange=(max(revChange))
maxLocation=(revChange.index(maxRevChange))
maxMonth=str(monthList[maxLocation])

print("Greatest Increase in Profits: $"+str(maxRevChange))
print("Month: "+maxMonth)

# The greatest decrease in losses (date and amount) over the entire period

minRevChange=(min(revChange))
minLocation=(revChange.index(minRevChange))
minMonth=str(monthList[minLocation])

print("Greatest Decline in Profits: $"+str(minRevChange))
print("Month: "+minMonth)
print("                                             ")

file = open("pyBank.txt","w") 
file.write(" \n")
file.write("Financial Analysis\n")
file.write("-----------------------------------------------\n")
file.write("Number of Months: "+str(num_lines)+"\n")
file.write("Net Profit/Loss for Period: $"+str(total)+"\n")
file.write("The average monthly change was: $"+avgChange+"\n")
file.write("Greatest Increase in Profits: $"+str(maxRevChange)+"\n")
file.write("Month: "+maxMonth+"\n")
file.write("Greatest Decline in Profits: $"+str(minRevChange)+"\n")
file.write("Month: "+minMonth+"\n")
 
file.close() 