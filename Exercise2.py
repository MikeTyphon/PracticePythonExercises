#! python3

#https://www.practicepython.org/


# Exercise 2. Odd or Even

'''
Ask the user for a number. Depending on whether the number is even or odd,
 print out an appropriate message to the user. Hint: how does an even / 
 odd number react differently when divided by 2?


'''

#number = int(input('please pick a number'))
number = int(input())
check = number%2



print(check)

if check>0:
	print('your number is odd')
else:
	print('your number is even')

p = input()