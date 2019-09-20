'''
---------------------------------------------------------------------------------------------------------------------
Name:			main.py

Version:		

Author:			Seth Pruitt

Description:	

Inputs:			

Returns:		

Comments:		

---------------------------------------------------------------------------------------------------------------------
'''

#IMPORT DEPENDENCIES
import os
import re

#INITIALIZATIONS
Script_Location = os.path.dirname(os.path.realpath(__file__)) + "/"

filepath1 = Script_Location + "raw_data/paragraph_1.txt"
filepath2 = Script_Location + "raw_data/paragraph_2.txt"

filepaths = [filepath1, filepath2]

for filepath in filepaths:
	txtobj = open(filepath, 'r')
	txtobj = txtobj.read()

	doclist = []
	sentencecount = 0

	for line in txtobj:
		if line != "\n":
			doclist.append(line)
		sentencecount += line.count('.') + line.count('!') + line.count('?')

	docstr = '' . join(doclist)
	sentences = re.split("(?<=[.!?]) +", docstr)
	for sen in sentences:

		print(sen + "\n")
	print("Sentence Count: " + str(sentencecount))
		

	