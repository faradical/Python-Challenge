'''
---------------------------------------------------------------------------------------------------------------------
Name:			main.py

Version:		

Author:			Donald Seth Pruitt

Description:	

Inputs:			

Returns:		

Comments:		

---------------------------------------------------------------------------------------------------------------------
'''

#IMPORT DEPENDENCIES
import csv
import os

#INITIALIZATIONS
#Path to script's parent directory
Script_Location = os.path.dirname(os.path.realpath(__file__)) + "/"
csvfile = Script_Location + "employee_data.csv"
outfile = Script_Location + "new_employee_data.csv"
openoutobj = open(outfile, mode='w', newline='')
outobj= csv.writer(openoutobj, delimiter=',')

#State abbreviation list
stateabbrevdict = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#FUNCTIONS DECLARATIONS
def CsvOpen(filename, *SkipHeader):
	obj = open(filename, newline='', encoding='UTF-8')
	CSVobj = csv.reader(obj, delimiter=',')
	
	if SkipHeader == "SkipHeader":
		next(CSVobj)

	return list(CSVobj)

#OPEN CSV
csvfile = Script_Location + "employee_data.csv"
EmployeeData = CsvOpen(csvfile)

#MANIPULATE DATA
#Update header with separate first and last name columns.
EmployeeData[0] = ["Emp ID","First Name","Last Name","DOB","SSN","State"]

for row in EmployeeData:
	if row != EmployeeData[0]:
		#Employee ID
		ID = row[0]

		#Name
		fullname = row[1].split(" ")
		firstname = fullname[0]
		lastname = fullname[1]

		#Date of Birth
		DOB = row[2].split("-")
		year = DOB[0]
		month = DOB[1]
		day = DOB[2]
		newDOB = month + "/" + day + "/" + year

		#SSN
		SSN = row[3].split("-")
		lastfour = SSN[2]
		newSSN = "***-**-" + lastfour

		#State
		state = row[4]
		stateabbrev = stateabbrevdict[state]

		#Build new row
		row = [ID, firstname, lastname, newDOB, newSSN, stateabbrev]
	
	#OUTPUT NEW CSV
	print(row)
	outobj.writerow(row)
