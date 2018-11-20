import random
from random import randint
import os
def int_to_file(filename, integers, known):
	#writes over the file you're sending with the modified bytes and between each byte it has a default number both people have; n
	looping=0
	FILE = open(filename, 'w')
	FILE = open(filename, 'a+b')
	knownByte = known.to_bytes((known.bit_length()//8)+1, byteorder = "big")
	# knownByte = known number in between each byte so that you can easily make a list for decrypting
	for looping in integers:
	#for num in integers:
		FILE.write(looping.to_bytes((looping.bit_length()//8)+1, byteorder = "big"))
		FILE.write(knownByte)
		#changes each integer into a byte
		#writes the bytes of the file
		#goes through each character of the file
def int_to_file_decrypt (filename, integers, path):
	os.chdir(path)
	#opens the directory that holds the file needed
	FILE = open(filename, 'w+')
	FILE = open(filename, 'a+b')
	for looping in integers
	#for num in integers:
		FILE = open(filename, 'a+b')
		FILE.write(looping.to_bytes((looping.bit_length()//8)+1, byteorder = "big"))
		#writes over the file with the decrypted characters
def file_to_array (filename, known):
	#this changes the file to an array of integers (each integer represents a character)
	#the number used to separate the character is turned into bytes so that the computer can compare
	bytelist = filename.split(known.to_bytes((known.bit_length()//8)+1), maxsplit = -1)
	#divides the list into an array in which each part is a byte for a different character, using the bytes for the testing
	intlist = [int.from_bytes(byteNum, byteorder = "big") for byteNum in bytelist]
	del inlist[len(intlist)-1]
	return intlist
def file_to_char(filename):
	characters = [(int.from_bytes(parts.encode(),byteorder = "big")) for parts in filename]
		#puts each character in the file into the array
		#converts each part of the file into utf-8 integers
		#converts each integer into bytes
	return characters
def gen_d (m, e):
	#generates the d value for the equation 
	hi = m, low = e
	r = hi%low
	#r for remainder from the high bound divided by low bound
	x = (hi-r)/low
	#gives the result of the division as an integer without the remainder
	aMult = 0-x, mMult = 1, oriA = 1, oriM = 0, hi = low
	low = r
	while low!= 1:
		r = hi%low
		x = (hi-r)/low
		tempM = mMult, tempA = aMult
		mMult = oriM - (x*mMult)
		aMult = oriA - (x*aMult)
		oriA = tempA, oriM = tempM
		hi = low
		low = r
	d = aMult
	if aMult <0:
		d = m+aMult
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
	#defines the upper boundary and lowerboundary for the generation of large prime numbers
	primeNum1 = gen_prime(down, up)
	primeNum2 = gen_prime(down, up)
	#two large prime numbers that are different from each other, but I need to add the comparison to each other
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
	bitlist = [((oldBits*2)**i) for oldBits in oldbitlist]
	newMess = 1
	for looping in range(len(bitlist)):
		#this is a method used so that the numbers aren't too big for the computer to do math with but remain accurate 
		if bitlist[looping] != 0:
		      for counter in range(looping);
				temp = (mess**2)%moded
				#takes it to the power of two before being moded and repeats because that is the same as
				#the temp to the power of 2^i and being moded for each of the bits that make up the exponent needed
			bitlist[looping] = temp
			#probable can just put newMess = newMess*temp%moded
			newMess = newMess*bitlist[looping]%moded
			#this works because a mod of a number is equal to it factors moded multiplied together and then moded again
	return newMess
