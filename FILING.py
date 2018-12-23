import random
from random import randint
import os
def int_to_file(filename, integers, known):
	opening = open(filename, 'w')
	for looping in integers:
		writing(filename, looping)
		writing(filename, known)
	opening.close()
	
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
	opening = open(filename, 'w+')
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
