#!/usr/bin/python

from random import randint
from sys import stdout

#Initialize a bunch of variables
lowers = 0
uppers = 0
numbers = 0
specials = 0
counter = 0

lowersList = range(97,123)
uppersList = range(65,91)
numbersList = range(48, 58)
specialsList = range(33,48) + range(58,65)+ range(91,97) + range(123,127)

asciiChars = lowersList + uppersList + numbersList + specialsList #This is the list of ASCII printable charachters, less the space charachter. I haven't tested passwords using ISO Latin-1 charachters
length = 16 #This is the length of the password to generate. The length is arbitrary. Anywhere between 16 and 32 bits is good. 

#Generate a random password. 
def generate(length):
	password = ''
	for j in range(length):
		password += chr(asciiChars[randint(0,len(asciiChars)-1)])
	return password

#Check that there are at least two types of characters. This is arbitrary.
while (lowers < 2 or uppers < 2 or numbers < 2 or specials < 2):
	
	#Reset the values for a fresh check on each iteration
	lowers = 0
	uppers = 0
	numbers = 0
	specials = 0
	output = generate(length)
	
	for i in range(len(output)):
		if ord(output[i]) in lowersList:
			lowers += 1

		if ord(output[i]) in uppersList:
			uppers += 1

		if ord(output[i]) in numbersList:
			numbers += 1

		if ord(output[i]) in specialsList:
			specials += 1

stdout.write(output)















	



