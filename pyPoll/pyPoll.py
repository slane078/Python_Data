import os
import csv
os.chdir(r'C:\Users\Sean\python-challenge\pyPoll')
csvfile = os.path.join('Resources', 'election_data.csv')


def pollreader():
    totvotes = len(votes)
    totkhan = len(khan)
    totcorrey = len(correy)
    totli= len(li)
    tottooley = len(tooley)
    khanvotes = round((totkhan / totvotes)*100)
    correyvotes = round((totcorrey / totvotes)*100)
    livotes = round((totli / totvotes)*100)
    tooleyvotes = round((tottooley / totvotes)*100)
    print(f"Election Results\n"
          f"-------------------------------\n"
          f"Total Votes: {totvotes}\n"
          f"-------------------------------\n"
          f"Khan: {khanvotes}.000% ({len(khan)})\n"
          f"Correy: {correyvotes}.000% ({len(correy)})\n"
          f"Li: {livotes}.000% ({len(li)})\n"
          f"O'Tooley: {tooleyvotes}.000% ({len(tooley)})\n"
          f"--------------------------------\n"
          f"Winner: {winner}\n"
          f"--------------------------------")
    file = open('Election_Results.doc', 'w')
    file.write(f"Election Results\n"
          f"-------------------------------\n"
          f"Total Votes: {totvotes}\n"
          f"-------------------------------\n"
          f"Khan: {khanvotes}.000% ({len(khan)})\n"
          f"Correy: {correyvotes}.000% ({len(correy)})\n"
          f"Li: {livotes}.000% ({len(li)})\n"
          f"O'Tooley: {tooleyvotes}.000% ({len(tooley)})\n"
          f"--------------------------------\n"
          f"Winner: {winner}\n"
          f"--------------------------------")
    print(f'\n Your election results have been saved as "Election_Results.doc"')

with open(csvfile, 'r') as pollcsv:
    pollread = csv.reader(pollcsv, delimiter=',')
    next(pollread)
    khan = []
    correy = []
    li = []
    tooley = []
    votes = []
    for x in pollread:
        votes.append('1')
        if x[2] == 'Khan':
            khan.append('x')
            # winner.append(int(1))
        elif x[2] == 'Correy':
            correy.append('x')
            # winner.append(int(2))
        elif x[2] == 'Li':
            li.append('x')
            # winner.append(int(3))
        elif x[2] == "O'Tooley":
            tooley.append('x')
            # winner.append(int(4))
    if len(khan) > len(li) and len(khan)> len(correy) and len(khan) > len(tooley):
        winner = 'Khan'
    elif len(li) > len(correy) and len(li) > len(tooley):
        winner = 'Li'
    elif len(correy) > len(tooley):
        winner = 'Correy'
    else:
        winner = "O'Tooley"
    pollreader()
