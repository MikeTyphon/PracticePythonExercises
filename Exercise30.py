#! python3

#https://www.practicepython.org/


# Exercise 30 Pick Word

'''
In this exercise, the task is to write a function that picks a 
random word from a list of words from the SOWPODS dictionary. 
Download this file and save it in the same directory as your Python code. 
This file is Peter Norvig’s compilation of the dictionary of words used 
in professional Scrabble tournaments. Each line in the file contains a single word.


Aside: what is SOWPODS
SOWPODS is a word list commonly used in word puzzles and games (like Scrabble for example). 
It is the combination of the Scrabble Player’s Dictionary and the Chamber’s Dictionary. 
(The history of SOWPODS is quite interesting, I highly recommend reading the 
Wikipedia article if you are curious.)

'''

import random



def ranword(a):
	list =[]
	for i in range(a):
		list.append(random.choice(open("sowpods.txt").readlines()).rstrip())
	print(list)
ranword(1)

