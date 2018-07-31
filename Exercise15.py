#! python3

#https://www.practicepython.org/


# Exercise 15. Reverse Word Order
'''
Write a program (using functions!) that asks the user for a long string 
containing multiple words. Print back to the user the same string, except
 with the words in backwards order.
'''

def streverse (string):
	string = string.split(' ')
	string = string[::-1]
	string = ' '.join(string)

	print(string)
	

streverse('taco tuesday')

