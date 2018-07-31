#! python3

#https://www.practicepython.org/


# Exercise 12. List Ends
'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
'''
list = ['taco', 'weeeeed', 23, 'tuesday', 795456, 45.56]



def firstlast(a):
	

	ends = [a[0],a[-1]]
	print(ends)




firstlast(list)
