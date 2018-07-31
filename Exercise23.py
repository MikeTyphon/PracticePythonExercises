#! python3

#https://www.practicepython.org/


# Exercise 23 File Overlap

'''
Given two .txt files that have lists of numbers in them, find the
numbers that are overlapping. One .txt file has a list of all prime 
numbers under 1000, and the other .txt file has a list of happy numbers 
up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any
other number. And yes, happy numbers are a real thing in mathematics - 
you can look it up on Wikipedia. The explanation is easier with an example,
which I will describe below.)


'''
print('start')

primenumbers = r'C:\Users\alexg\Dropbox\Files\Python Scripts\Practice\PracticePythonExercises\Textfiles\primenumbers.txt'


happynumbers = r'C:\Users\alexg\Dropbox\Files\Python Scripts\Practice\PracticePythonExercises\Textfiles\happynumbers.txt'

print(primenumbers)
print(happynumbers)
primelist = []
happylist = []

with open(primenumbers, 'r') as pfile:
	while p_text:
		primelist.append(int(p_text))
		line = pfile.readline()

print(primelist)

with open(happynumbers, 'r') as hfile:
	h_text = hfile.readline()
	while line:
		happylist.append(int(line))
		line = hfile.readline()

overlap = []

for i in primelist:
	if i in happylist:
		overlap.append(i)

print(overlap)

print('end')
