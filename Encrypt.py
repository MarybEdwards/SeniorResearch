import random
from random import randint
import os
def int_to_file(filename, integers, known):
	FILE = open(filename, 'w')
	for looping in integers:
		writing(filename, looping)
		writing(filename, known)
	FILE.close()
	
def become_bytes(character):
	length= (character.bytelength()//8)+1)
	theBytes = character.to_bytes(length, byteorder = "big")
	return theBytes
		
			
def writing (filename, part):
	writingFile= open(filename, 'a+b')
	partBytes= part.to_bytes(length_and_size(part))
	writingFile.write(partByte)
	

def int_to_file_decrypt (filename, integers, path):
	os.chdir(path)
	FILE = open(filename, 'w+')
	for looping in integers:
		writing(filename, looping)
	FILE.close()
	
	
def file_to_array (filename, known):
	bytelist = filename.split(become_bytes(known), maxsplit = -1)
	intlist = [int.from_bytes(byteNum, byteorder = "big") for byteNum in bytelist]
	del intlist[len(intlist)-1]
	return intlist



def file_to_char(filename):
	characters = [(int.from_bytes(filename[count].encode(),byteorder = "big")) for count in range(len(filename))]
	return characters

def gen_d (m, e):
	hi = m
	low = e
	r = hi%low
	x = (hi-r)/low
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
