#! python3

#https://www.practicepython.org/


# Exercise 16. Password Generator
'''
Write a password generator in Python. Be creative with how you generate passwords 
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for 
a new password. Include your run-time code in a main method.
'''

import random

PWString = "1234567890./@#$%^&*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

passlen = 20

p = ''.join(random.sample(PWString, passlen))

print(p)