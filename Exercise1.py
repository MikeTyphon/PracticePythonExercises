#! python3

#https://www.practicepython.org/


# Exercise 1. Character Input

'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them 
that tells them the year that they will turn 100 years old.

'''

import datetime

print('What is your name?')

name = input()

print('What is your age?')

age = int(input())

#age = 23
k = input()


current_year = int(datetime.datetime.now().year)

YearAge100 = current_year - age + 100 

print(name + ', you will be 100 years old in: ' + str(YearAge100))

p = input()