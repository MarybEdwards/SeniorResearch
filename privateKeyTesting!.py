n= 6057448570781
e= 43478616355.0
import Encrypt
from Encrypt import int_to_file
from Encrypt import file_to_char
from Encrypt import file_to_array
from Encrypt import int_to_file_decrypt
from Encrypt import mod_math
def encrypt(filename, f):
	listnum = file_to_char(f)
	#takes the file and puts into integers to mess around with
	listnum = [mod_math(count, e, n) for count in listnum]
	#preforms the math that screws around with the bits so its unreadable
	int_to_file(filename, listnum, n)
	#overrides the file with the bits that are messed up
def decrypt (f, filename, path):
	numlist = file_to_array(f, n)
	#exact same procedure as above, except the int_to_file_decrypt instead 
	#of without the _decrypt so the dividers inserted 
	listnum = [mod_math(count, e, n) for count in numlist]
	int_to_file_decrypt(filename, listnum, path)
