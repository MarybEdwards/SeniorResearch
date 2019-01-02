import random
from random import randint
import os
readMode = "'r'"
writeMode = "'w'"
writeAddMode = "'w+'"
appendByteMode = "'a+b'"
def int_to_file(filename, integers, known):
	opening = open(filename, writeMode)
	for looping in integers:
		writing(filename, looping)
		writing(filename, known)
	opening.close()
	
def become_bytes(character):
	length= (character.bytelength()//8)+1)
	theBytes = character.to_bytes(length, byteorder = "big")
	return theBytes
		
			
def writing (filename, part):
	writingFile= open(filename, appendByteMode)
	partBytes= part.to_bytes(length_and_size(part))
	writingFile.write(partByte)
	

def int_to_file_decrypt (filename, integers, path):
	os.chdir(path)
	opening = open(filename, writeMode)
	for looping in integers:
		writing(filename, looping)
	opening.close()
	
	
def integer_from_bytes(byteNum):
	integer = int.from_bytes(byteNum, byteorder = "big")
	return integer
	
def file_to_array (filename, known):
	bytelist = filename.split(become_bytes(known), maxsplit = -1)
	intlist = [intger_from_bytes(byteNum for byteNum in bytelist]
	del intlist[len(intlist)-1]
	return intlist



def file_to_char(filename):
	characters [integer_from_bytes(filename[count].encode) for count in range(len(filename))]
	return characters

def write_to_skely (number1, number2, filename):
	skely = open('skeleton.txt', readMode).read()
	fileRead = open(filename, writeAddMode)
	fileRead.write("n= " + number1 + "\ne= " + number2 + "\n" +skely)
	fileRead.close()
	skely.close()
				   
def change_ip_address (ipAdress):
	newAddress = ipAdress.replace(".", "!")
	return newAdress
				     
