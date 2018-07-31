#! python3

#https://www.practicepython.org/


# Exercise 3. List Less Than Ten

'''
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.


'''


list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

lessthan5 = []


for a in list:
	if a < 5:
 		print('+' + str(a))
 		lessthan5.append(a)
	else:
 		print(a)

print(lessthan5)