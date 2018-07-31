#! python3

#https://www.practicepython.org/


# Exercise 13. 
'''
Write a program that asks the user how many Fibonnaci numbers to generate and
 then generates them. Take this opportunity to think about how you can use functions. 
 Make sure to ask the user to enter the number of numbers in the sequence to generate.
 (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the 
 sequence is the sum of the previous two numbers in the sequence. The sequence looks 
 like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def fibonacci(n):
	a = 1
	b = 1
	x = 0
	c = 0
	sequence = [1,1]


	while x != n:
		c = a + b
		a = b
		b = c

		sequence.append(c)

		x += 1

	print(sequence)

fibonacci(10)