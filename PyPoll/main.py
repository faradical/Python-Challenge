#PyPoll main.py V2
'''
---------------------------------------------------------------------------------------------------------------------
Name:			main.py

Version:		

Author:			Donald Seth Pruitt

Description:	This script parses election_data.csv to calculate comment specified values.

Inputs:			None.

Returns:		Object in format:

					Election Results
					-------------------------
					Total Votes: 3521001
					-------------------------
					Khan: 63.000% (2218231)
					Correy: 20.000% (704200)
					Li: 14.000% (492940)
					O'Tooley: 3.000% (105630)
					-------------------------
					Winner: Khan
					-------------------------


Comments:		9/14/2019 -	Began writing script. I am very tired. I think I have been tired for a long time.
				
				9/15/2019 -	This one was hard. I struggled greatly with discovering that object created by the 
							csv.reader() function seems to only be iterable one time after it was created and I 
							still do n0t understand why this is. I have also had great difficulty in finding the 
							most efficient way to iterate over the data. Attempts to perform a single loop through
							the csv for all of the data required from it in one go have been unsuccessful. I do not
							know anything about computer science.

				9/15/2019 -	I have finally found a way to improve the efficiency of the program. By introducing a 
							new list of only candidate names and comparing each new candidate to it, I am able to 
							include the parsing for voting data within the same single for loop. This single for 
							loop allows me to cut the average runtime from 11.14 to 4.6 seconds.

---------------------------------------------------------------------------------------------------------------------
'''

#Import Modules
import csv
import os
Script_Location = os.path.dirname(os.path.realpath(__file__)) + "/"

#Variable Initializations
filename = Script_Location + "Resources/election_data.csv"
TotalVotes = 0
CandidateList = []
CandidateNameList = []
WinnerVotes = 0

#Define Function for building iterable object from CSV
def CsvOpen(filename):
	CSVobj = open(filename, newline='', encoding='UTF-8')
	ELECobj = csv.reader(CSVobj, delimiter=',')

	next(ELECobj)
	return list(ELECobj)

#Open file and read data into object
ELECobj = CsvOpen(filename)
#TotalVotes = len(ELECobj)
#Parse data by row from 3 colums (Voter ID, County, and Candidate) for:
#CandidateList.append({'name':ELECobj[0][2],'votes':0,'percentage':0})

for row in ELECobj:
	#The total number of votes cast
	TotalVotes += 1

	#A complete list of candidates who received votes
	NewCandidate = {'name':row[2],'votes':0,'percentage':0}
	
	if NewCandidate['name'] not in CandidateNameList:
		CandidateList.append(NewCandidate)
		CandidateNameList.append(NewCandidate['name'])

	#The total number of votes each candidate won
	for Candidate2 in CandidateList:
		if Candidate2['name'] == row[2]:
			Candidate2['votes'] += 1

	'''NamePresent = False

	for Candidate in CandidateList:
		if NewCandidate['name'] == Candidate['name']:
			NamePresent = True
			Candidate['votes'] += 1

	if NamePresent == False:
		NewCandidate['votes'] += 1
		CandidateList.append(NewCandidate)'''

#Gather data, Perform final calculations
for Candidate in CandidateList:
	#The percentage of votes each candidate won
	Candidate['percentage'] = Candidate['votes'] * 100 / TotalVotes

	#The winner of the election based on popular vote.
	if Candidate['votes'] > WinnerVotes:
		WinnerVotes = Candidate['votes']
		WinnerName = Candidate['name']

#Build output
Results = "Election Results\n-------------------------\nTotal Votes: {}\n-------------------------\n".format(TotalVotes)
for Candidate in CandidateList:
	Results += "{}: {:.3f}% ({})\n".format(Candidate['name'],float(round(Candidate['percentage'], 3)),Candidate['votes'])

Results += "-------------------------\nWinner: {}\n-------------------------".format(WinnerName)

#Write to standard Output
print(Results)

#Write to File.
OutFile = Script_Location + "Resources/Election_Results.txt"
OutFile = open(OutFile, "w")
OutFile.write(Results)
OutFile.close
