#! python3

#https://www.practicepython.org/


# Exercise 24 Draw a Game Board

'''
Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes 
(8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, 
and draw it for them to the screen using Python’s print statement.

Remember that in Python 3, printing to the screen is accomplished by

  print("Thing to show on screen")



'''

import random as ra



def boardsize(board_height,board_width):

	print('height = ' + str(board_height) + '\n' +'width = ' + str(board_width))
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	x = 0
	print(str(alphabet[0:board_width]))

	while x!= board_height:

		print(' --- ' * board_width)
		print('|    '* board_width + '|' +' '+ str(x+1))
		x+=1

	print(' --- '* board_width)

	
boardsize(ra.randint(1,10), ra.randint(1,10))

print('-------------------------------------------------')

