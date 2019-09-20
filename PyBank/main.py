'''
---------------------------------------------------------------------------------------------------------------------
Name:			main.py

Version:		

Author:			Donald Seth Pruitt

Description:	This script reads budget_data.csv to calculate:

				-The total number of months included in the dataset
				-The net total amount of "Profit/Losses" over the entire period
				-The average of the changes in "Profit/Losses" over the entire period
				-The greatest increase in profits (date and amount) over the entire period
				-The greatest decrease in losses (date and amount) over the entire period

Inputs:			None.

Returns:		Object to standard out and textfile budget_data_output.txt with the following parameters and format:
				
				Financial Analysis
				----------------------------
				Total Months: 86
				Total: $38382578
				Average  Change: $-2315.12
				Greatest Increase in Profits: Feb-2012 ($1926159)
				Greatest Decrease in Profits: Sep-2013 ($-2196167)

Comments:		9/13/2019 - Began writing script.

---------------------------------------------------------------------------------------------------------------------
'''

import csv

#Variable initializations
RowCount = 0
GrossProfit = 0
ProfitChangeSum = 0
GreatestProfit = 0
GreatestLoss = 0

#Read in csv file
csvpath = "budget_data.csv"

with open(csvpath, newline='', encoding='UTF-8') as csvfile:
	csvreader = csv.reader(csvfile,delimiter=',')

	#Skip header row.
	next(csvreader)

	#Parse Data for desired values.
	for row in csvreader:
		
		#Check data for empty rows.
		if row != "":

			#Number of months stored in variable RowCount.
			RowCount += 1

			#Gross profit/loss calculation.
			MonthlyProfit = int(row[1])
			GrossProfit += MonthlyProfit

			#Change of profit between months.
			if RowCount != 1:
				ProfitChange = MonthlyProfit - OldMonthlyProfit
				ProfitChangeSum += ProfitChange

				#Greatest profit. Store date and amount in variable.
				if ProfitChange > GreatestProfit:
					GreatestProfit = ProfitChange
					GreatestProfitDate = row[0]

				#Greatest loss. Store date and amount in variable.
				if ProfitChange < GreatestLoss:
					GreatestLoss = ProfitChange
					GreatestLossDate = row[0]

			OldMonthlyProfit = MonthlyProfit

			#File name information. Not relevant to challenge.
			if RowCount == 1:
				FirstDate = row[0]

			LastDate = row[0]

#Calculate Average Change
AverageChange = ProfitChangeSum / (RowCount - 1)

#Build object with gathered data.
FinancialAnalysis = "Total Months: {}\nTotal: ${}\nAverage  Change: ${:.2f}\nGreatest Increase in Profits: {} (${})\nGreatest Decrease in Profits: {} (${})".format(RowCount,GrossProfit,AverageChange,GreatestProfitDate,GreatestProfit,GreatestLossDate,GreatestLoss)

#Write object to Standard output.
print(FinancialAnalysis)

#Create text file and write object to it.
FileName = "budget_data_output_" + FirstDate + "-" + LastDate +".txt"
OutFile = open(FileName, "w")
OutFile.write(FinancialAnalysis)
OutFile.close