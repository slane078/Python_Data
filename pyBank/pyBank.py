import os
import csv
# @Update average change in months - for loop revenue to run avgchange.append(row - (row +1))
os.chdir(r'C:\Users\Sean\python-challenge\pybank')
bankCSV = os.path.join('budget_data.csv')

# Function to run arithmetic and print/save analysis
def revreader():
    monthtracker = len(dates)
    revtracker = sum(revenue)
    hincrease = max(revenue)
    hdecrease = min(revenue)
    totchange = str(round((sum(avgchange) / len(avgchange)), 2))
    idates = revenue.index(hincrease)
    ddates = revenue.index(hdecrease)
    maxrev = revenue[idates] - revenue[idates - 1]
    minrev = revenue[ddates] - revenue[ddates - 1]
    mincrease = dates[idates]
    mdecrease = dates[ddates]
    print(f"Financial Analysis\n "
          f"------------------------\n "
          f"Total Months: {monthtracker}\n "
          f"Total: ${revtracker}\n "
          f"Average Change: {totchange}\n "
          f"Greatest Increase in Profits: {mincrease} (${maxrev})\n "
          f"Greatest Decrease in Profits: {mdecrease} (${minrev})")
    file = open("Revenue_Analysis.doc", "w")
    file.write(f"Financial Analysis\n "
               f"------------------------\n "
               f"Total Months: {monthtracker}\n "
               f"Total: ${revtracker}\n "
               f"Average Change: {totchange}\n "
               f"Greatest Increase in Profits: {mincrease} (${maxrev})\n "
               f"Greatest Decrease in Profits: {mdecrease} (${minrev})")
    print("\nYour analysis has been saved as: Revenue_Analysis.doc")

# opening file to read
with open(bankCSV, 'r') as bankFile:
    bankRead = csv.reader(bankFile, delimiter=',')
    next(bankRead) # Skip first line(header) in csv
    # Defining necessary tables
    dates = []
    revenue = []
    avgchange = []
    for row in bankRead:
        revenue.append(row[1])
        dates.append(row[0])
    revenue = list(map(int, revenue))
    for x in range(len(revenue)-1):
        avgchange.append(revenue[x+1] - revenue[x])
    revreader()
