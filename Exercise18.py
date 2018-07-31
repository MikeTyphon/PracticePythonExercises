#! python3

#https://www.practicepython.org/


# Exercise 18. Cow and Bull

'''
Create a program that will play the “cows and bulls” game with the user.
The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they 
have a “cow”. For every digit the user guessed correctly in the wrong place 
is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” 
they have. Once the user guesses the correct number, the game is over. Keep track of the 
number of guesses the user makes throughout the game and tell the user at the end.
'''

import random 
guesscount = 0
guess = 1234
guess = str(guess)
#guess = str(input())
number =random.randint(1000,9999)
number = str(number)
print('number to guess is' + number)

x=0
while number != guess:
	bulls = 0
	cows = 0

	guess = str(random.randint(1000,9999))
	print('my guess is: ' + guess)
	for i in guess:
		if i in number:
			bulls +=1
		elif i not in number:
			cows += 1
	print(str(bulls) + ' bulls')
	print(str(cows) + ' cows')

	x+=1
	guesscount +=1
	print('the correct number is: ' + number)
	print('attempt: '+ str(x))


print('done')
