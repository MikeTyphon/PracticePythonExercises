#! python3

#https://www.practicepython.org/


# Exercise 11. Check Primality Functions

'''
Ask the user for a number and determine whether the number is prime or not.
 (For those who have forgotten, a prime number is a number that has no divisors.). 
 You can (and should!) use your answer to Exercise 4 to help you. 
 Take this opportunity to practice using functions, described below.
'''

def isprime(number):
	#base primes

	if number == 1:
		prime = False
	elif number == 2:
		prime = True

	#all other primes
	else:
		prime = True
		for checknum in range(2, number):
			if number % checknum == 0:
				prime = False
				print(checknum)
				break
	
	if prime == True:
		print(str(number) + ' is a prime number')
	else:
		print(str(number) + ' is not a prime number')


def allprimes(low, high):
	Primes = []
	for num in range(low, high +1):
		prime = True
		for i in range(2, num):
			if num % i == 0:
				prime = False
		if prime == True:
			#print(num)
			Primes.append(num)

	print(Primes)






allprimes(60,70)
'''
     for num in range(2,101):
          prime = True
          for i in range(2,num):
              if (num%i==0):
                prime = False
          if prime == True:
            print(num)
         
'''