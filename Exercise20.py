#! python3

#https://www.practicepython.org/


# Exercise 20. Element Search

'''
Write a function that takes an ordered list of numbers (a list where the
elements are in order from smallest to largest) and another number. The
function decides whether or not the given number is inside the list and
returns (then prints) an appropriate boolean.
'''

a = [1,2,3,4,5,6,7,8,45,67,78,96]

def elem_search(b):
	if b in a: 
		print(True)
	else:
		print(False)
		


elem_search(34)
