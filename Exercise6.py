  #! python3

#https://www.practicepython.org/


# Exercise 6. String Lists

'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

#checking if a string is a palindrome function

def ispalindrome(s):
	s = s.replace(" ","")
	
	if s == s[::-1]:
		print('yes')
	else:
		print('no')



ispalindrome('nargle flip')


def makespalindrome(m):
	m = str(m) + ' ' + str(m[::-1])
	print(m)

makespalindrome('taco')