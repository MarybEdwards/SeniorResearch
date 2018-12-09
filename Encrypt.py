import random
from random import randint
import os
def int_to_file(filename, integers, known):
	#writes over the file you're sending with the modified bytes and between each byte it has a default number both people have; n
	#filename is the file that is being written over
	#integers is the list of numbers that has been modified to encode the file 
	#known is the number n which has been shared between both people and is used like a comma to seperate each byte for easier decoding later
	FILE = open(filename, 'w')
	FILE = open(filename, 'a+b')
	# opens the file so that it can be written and added onto in bytes
	knownByte = known.to_bytes((known.bit_length()//8)+1, byteorder = "big")
	#knownByte = known number in between each byte so that you can easily make a list for decrypting
	for looping in integers:
	#goes through each number in the list of "integers"
		FILE.write(looping.to_bytes((looping.bit_length()//8)+1, byteorder = "big"))
		#adds the byte form of each integer to the file 
		FILE.write(knownByte)
		#adds in the byte form of the known number as a default comma
	FILE.close()
def int_to_file_decrypt (filename, integers, path):
	#filename is the file that is being decrypted
	#integers is the list of numbers that has been modified to the correct integer interpretation of the characters
	#path is the way to get to the file so that it can be directly written over
	os.chdir(path)
	#opens the directory that holds the file needed
	FILE = open(filename, 'w+')
	#writes over everything that already existed in the file, which is no longer needed because that information was transferred to integers
	FILE = open(filename, 'a+b')
	#opens the file so that it can be added to in bytes
	for looping in integers:
	#for num in integers:
		FILE = open(filename, 'a+b')
		FILE.write(looping.to_bytes((looping.bit_length()//8)+1, byteorder = "big"))
		#writes over the file with the decrypted characters in byte form
	FILE.close()
def file_to_array (filename, known):
	#This turns the file into an array of integers, each of which represents a character for decryption
	#filename is the file being decrypted
	#known is the number that was used as a comma when encrypting the file, it is a number both keys share
	bytelist = filename.split(known.to_bytes((known.bit_length()//8)+1, byteorder = "big"), maxsplit = -1)
	#Splits the file into an array of bytes and it knows where to split by using the known as a reference point
	intlist = [int.from_bytes(byteNum, byteorder = "big") for byteNum in bytelist]
	#converts the array from bytes to integers
	del intlist[len(intlist)-1]
	#there is an extra blank spot at the end of the list that can come up with an error if left in the list, so it is removed
	return intlist
def file_to_char(filename):
	characters = [(int.from_bytes(filename[count].encode(),byteorder = "big")) for count in range(len(filename))]
		#puts each character in the file into the array
		#converts each part of the file into utf-8 integers
		#converts each integer into bytes
	return characters
def gen_d (m, e):
	#generates the d value for the equation by finding e^-1modm
	hi = m
	#the larger number is the m value and that is the number being moded by e
	low = e
	#e is the smaller number m is being moded by
	r = hi%low
	#r for remainder of the hi/low, which is equal to hi moded by low
	x = (hi-r)/low
	#gives the result of the division as an integer without the remainder
	#equation used is: r=m-x*a
	aMult = 0-x
	mMult = 1
	#r=mMult*hi*M+aMult*low*A
	#^^where M and A are variables
	oriA = 1
	oriM = 0
	hi = low
	low = r
	while low!= 1:
		r = hi%low
		x = (hi-r)/low
		tempM = mMult
		tempA = aMult
		mMult = oriM - (x*mMult)
		aMult = oriA - (x*aMult)
		#r= hiM-xlowA
		#r = hi-(previousR*x) which ends up being r=(previousMcoefficient-(x*currentMcoefficient))m+(previousAcoefficient-(x*currentAcoefficient))a
		#this is because you sub in the previous equation
		oriA = tempA
		oriM = tempM
		hi = low
		low = r
	d = aMult
	if aMult <0:
		d = m+aMult
		#ensures that this value is positive 
	return d
def gen_e (m):
	check = 2 
	e = 1003242
	while check <= (e**(1/2)):
		#checks to ensure that e and m have no common factors 
		#it is raised to the power of 1/2 because if it doesn't have any common factors until its square root, it won't have any
		if e%check ==0 and m% check ==0:
			e +=1
			check = 2
		else:
			check +=1
	return e
def gen_key():
	up = 10000000
	down = 100000
	same = 0 
	#defines the upper boundary and lowerboundary for the generation of large prime numbers
	while same==0:
		primeNum1 = gen_prime(down, up)
		primeNum2 = gen_prime(down, up)
		if primeNum1!=primeNum2:
			same = 1
	#two large prime numbers that are different from each other
	m, n= gen_m_n (primeNum1, primeNum2)
	e = gen_e(m)
	d = gen_d (m, e)
	#n is the value shared between both private and public keys, but d is for the private key and e is for the public key
	return n, e, d
def gen_m_n(num1, num2):
	m = (num1-1)*(num2-1)
	n = num1*num2
	return m, n
def gen_prime (down, up):
	prime = random.randint(down, up)
	check = 2
	while check < (prime**(1/2)):
		#checks every possible factor up until the square root, at which it would begin repeating itself ensuring the creation of
		#of a prime number without taking too much time checking factors
		if prime%check ==0 and prime!=up:
			prime +=1
			check = 2
		else:
			check +=1
	return prime
def mod_math (mess, exp, moded):
	oldbitlist = list()
	while exp!=0:
		oldbitlist.append (exp%2)
		exp = (exp-(exp%2))/2
		# give binary stuff like 1, 2, 4, 8, 16, 32 to break the number into more manageable pieces
	bitlist = [(oldbitlist[count]*2)**count for count in range(len(oldbitlist))]
	newMess = 1
	for looping in range(len(bitlist)):
		#this is a method used so that the numbers aren't too big for the computer to do math with but remain accurate 
		if bitlist[looping] != 0:
                    temp = mess
                    for counter in range(looping):
                        temp=(temp**2)%moded
                        #takes it to the power of two before being moded and repeats because that is the same as
                        #the temp to the power of 2^i and being moded for each of the bits that make up the exponent needed
		    #probable can just put newMess = newMess*temp%moded
                    newMess=newMess*temp%moded
		    #this works because a mod of a number is equal to it factors moded multiplied together and then moded again
	return newMess
