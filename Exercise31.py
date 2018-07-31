#! python3

#https://www.practicepython.org/


# Exercise 31 Guess Letters

'''
Let’s continue building Hangman. In the game of Hangman, a clue word is given by the 
program that the player has to guess, letter by letter. The player guesses one letter
 at a time until the entire word has been guessed. (In the actual game, the player can
  only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the
logic that asks a player to guess a letter and displays letters in the clue word that
were guessed correctly. For now, let the player guess an infinite number of times until
they get the entire word. As a bonus, keep track of the letters the player guessed and 
display a different message if the player tries to guess that letter again. Remember to 
stop the game when all the letters have been guessed correctly! Don’t worry about choosing 
a word randomly or keeping track of the number of guesses the player has remaining - we will 
deal with those in a future exercise.


'''

import random
import numpy as np
words =[]
for i in range(1):
	words.append(random.choice(open("sowpods.txt").readlines()).rstrip()) # picks random word

words = words[0] #converts the random word into a string
word = []
print(words)

for i in words:
	word.append(i) # converts the string into a list

word = np.array(word)


string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #the alphabet as a string
alphabet = []
for i in string:
	alphabet.append(i) #converts alphabet string into list because I was too lazy to find my alphabet as list already made


print(alphabet)

print(word)
#shows we have made our alphabet and target word lists


#Now we will begin guessing and removing letters which have been guessed both from target and alphabet

guess = random.choice(alphabet)

charcorrect = []
charwrong = []

wordbank =[]
ii = []
for i in range(len(word)):
	wordbank.append('_ ')

print(''.join(wordbank))

print(guess)

if guess in alphabet:
	alphabet.remove(guess)
else:
	print('You have guessed that letter')

if guess not in word:
	charwrong.append(guess)
else:
	ii = (np.where(word == guess)[0])
	wordbank.place(guess, ii)
	print(ii)




print(alphabet)
print(word)
print('The word does not contain the letters' + str(charwrong))
print(ii)

# code has gotten pretty messy, come back to another  time when I have more time to kill
# pretty fun though