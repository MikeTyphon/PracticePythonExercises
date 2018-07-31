#! python3

#https://www.practicepython.org/


# Exercise 4. Divisors

'''
Create a program that asks the user for a number and then prints out a list of all
the divisors of that number. (If you don’t know what a divisor is, it is a number that divides
evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

'''

number = int(input('Input a number here: '))

#number = 155

numdivisors = []

for div in range(1, int(number + 1)):
	if number % div == 0:
		numdivisors.append(div)
		print('+' + str(div))
	else:
		continue


print(numdivisors)

