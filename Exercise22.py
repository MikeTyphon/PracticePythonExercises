#! python3

#https://www.practicepython.org/


# Exercise 22  Element Search

'''
Given a .txt file that has a list of a bunch of names, count
how many of each name there are in the file, and print out the
results to the screen. I have a .txt file for you, if you want to use it!

'''

import re


mam = r'C:\Users\alexg\Dropbox\Files\Python Scripts\TextFiles\MarcusAurelius_Meditations.txt'

with open(mam, 'r') as openfile:
	all_text = openfile.read()

mamRegex = re.compile(r'Marcus Aurelius')

print(re.compile(all_text))
