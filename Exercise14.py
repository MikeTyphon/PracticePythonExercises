#! python3

#https://www.practicepython.org/


# Exercise 14. List Remove Duplicates
'''
Write a program (function!) that takes a list and returns a new list 
that contains all the elements of the first list minus all the duplicates.
'''



def removedups(list):
	cleanlist = []
	for i in list:
		if i not in cleanlist:
			cleanlist.append(i)
	print(cleanlist)
	return cleanlist
a = [1,2,3,4,5,5,5,5,4]

removedups(a)


