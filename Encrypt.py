import random
from random import randint
import os
def int_to_file(filename, integers, n):
	#writes over the file you're sending with the modified bytes and between each byte it has a default number both people have; n
	i=0
	f = open(filename, 'w')
	f = open(filename, 'a+b')
	g = n.to_bytes(7, byteorder = "big")
	# g = known number in between each byte so that you can easily make a list for decrypting
	while i < len(integers):
		byted = integers[i].to_bytes(10,byteorder = "big")
		#changes each integer into a byte
		f.write (byted)
		f.write(g)
		#writes the bytes of the file
		f.read()
		i = i+1
		#goes through each character of the file
def int_to_file_decrypt (filename, integers, path):
	os.chdir(path)
	#opens the directory that holds the file needed
	f = open(filename, 'w+')
	f = open(filename, 'a+b')
	i = 0
	while i < len(integers):
		byted= integers [i].to_bytes(10, byteorder = "big")
		f = open(filename, 'a+b')
		#writes over the file with the decrypted characters
		f.write (byted)
		i = i+1
def file_to_array (f, n):
	#this changes the file to an array of integers (each integer represents a character)
	testing = n.to_bytes(7, byteorder = "big")
	#the number used to separate the character is turned into bytes so that the computer can compare
	bytelist = f.split(testing, maxsplit = -1)
	#divides the list into an array in which each part is a byte for a different character, using the bytes for the testing
	i = 0 
	# intlist = [int.from_bytes(bytelist[i], byteorder = "big"), for i in bytelist
	#check to replace below)
	while i<len(bytelist):
		p = int.from_bytes(bytelist[i], byteorder = "big")
		#changes the character bytes into integers
		bytelist[i] = p
		i = i+1
	del bytelist[len(bytelist)-1]
	return bytelist
#pretty sure this isn't used below so probably delete file to int 
#def file_to_int(h):
#	i = 0
#	h = h.split()
#	integers = list()
#	while i<len(h):
#		p = int.from_bytes(h[i], byteorder = "big")
#		inegers.append(p)
#		i = i+1
#	return integers
def file_to_char(h):
	#the file is called h (I will change it to a better name)
	i = 0
	characters = list()
	while i < len(h):
		#runs for the until the entire file has been put into the array
		characters.append(h[i])
		#puts each character in the file into the array
		characters[i]= characters[i].encode()
		#converts each part of the file into utf-8 integers
		characters[i]= int.from_bytes(characters[i], byteorder = "big")
		#converts each integer into bytes
		i = i+1
	return characters
def gen_d (m, e):
	#generates the d value for the equation 
	hi = m
	low = e
	r = hi%low
	#r for remainder from the high bound divided by low bound
	x = (hi-r)/low
	#gives the result of the division as an integer without the remainder
	aMult = 0-x
	mMult = 1
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
		oriA = tempA
		oriM = tempM
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
		if e%check ==0 and m% check ==0:
			e = e+1
			check = 2
		else:
			check = check +1
	return e
def gen_key():
	up = 10000000
	down = 100000
	#defines the upper boundary and lowerboundary for the generation of large prime numbers
	p = gen_prime(down, up)
	q = gen_prime(down, up)
	#two large prime numbers that are different from each other, but I need to add the comparison to each other
	m, n= gen_m_n (p, q)
	e = gen_e(m)
	d = gen_d (m, e)
	#n is the value shared between both private and public keys, but d is for the private key and e is for the public key
	return n, e, d
def gen_m_n(p, q):
	m = (p-1)*(q-1)
	n = p*q
	return m, n
def gen_prime (down, up):
	p = random.randint(down, up)
	check = 2
	while check < (p**(1/2)):
		#checks every possible factor up until the square root, at which it would begin repeating itself ensuring the creation of
		#of a prime number without taking too much time checking factors
		if p%check ==0 and p!=up:
			p = p+1
			check = 2
		else:
			check = check +1
	return p
def mod_math (mess, exp, moded):
	oldbitlist = list()
	while exp!=0:
		oldbitlist.append (exp%2)
		exp = (exp-(exp%2))/2
		# give binary stuff like 1, 2, 4, 8, 16, 32 to break the number into more manageable pieces
	#bitlist = [((oldbitlist(i)*2)**i) for i in oldbitlist]
	#see if above works and delete below
	i = 0
	while i<len(bitlist):
		bitlist [i] = oldbitlist[i]*2)**i
		i = i+1
	i=0
	newMess = 1
	while i< len(bitlist):
		#this is a method used so that the numbers aren't too big for the computer to do math with but remain accurate 
		if bitlist[i] != 0:
			temp = mess
			counter = 0
			while counter <i:
				temp = temp**2
				#takes it to the power of two before being moded and repeats because that is the same as
				#the temp to the power of 2^i and being moded for each of the bits that make up the exponent needed
				temp = temp%moded
				counter = counter +1
			bitlist[i] = temp
			#probable can just put newMess = newMess*temp%moded
			newMess = newMess*bitlist[i]%moded
			#this works because a mod of a number is equal to it factors moded multiplied together and then moded again
		i = i+1
	return newMess
