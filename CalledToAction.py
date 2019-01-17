import subprocess
from subprocess import call
import sys
from sys import modules
import os
import getpass
import Math
from Math import gen_key
import FTPStuff
from FTPStuff import ftp_login
from FTPStuff import ftp_placing
from FTPStuff import get_other_ip_ad

READ_MODE = "'r'"
READ_BINARY_MODE = "'rb'"
PATH_ASK = "'What was the path provided? '"
CURRENT = os.getcwd
task = input('What would you like to do? \nEncrypt a file (e), decrypt a file(d), or send a public key (k)? ')
#this decides what the program will do
if task == "e":
	#process for encrypting a file
	filename = input('What file would you like to encrypt? ')
	#finds the file needed to be encrypted
	ip_ad = get_other_ip_ad()
	#asks for the other end of this correspondance
	path = input(PATH_ASK)
	#the direction the computer needs to go to get to the file
	encryption = "publicKey" + change_ip_address(ip_ad)
	#looks for the key for the specific person 
	module = __import__(encryption).encrypt
	#loads the instructions from the key and runs them
	os.chdir(path)
	#changes directories to the file so the file can be read
	fileRead = open(filename, READ_BINARY_MODE).read()
	#reads file and loads what it says into the program
	os.chdir(CURRENT)
	#moves directory back to where program is stored so it can call on different parts of the program
	module(filename, fileRead)
	#THE PROGRAM FOR ENCRYPTING IS CALLED!!!! YAY
	ftp= ftp_login(ip_ad)
	#connects to other computer
	ftp_placing (ftp, filename, fileRead)
	#places file in other computer
	os.remove(filename)
	#removes the encrypted form of the file from this computer so you only have the plaintext file
if task == "d":
	#decrypts a file that has been recieved
	filename = input('What file would you like to decrypt? ')
	#identifies encrypted file
	ip_ad = get_other_ip_ad()
	#asks for the sender so they know which key to use
	path = input (PATH_ASK)
	#finds the path back to the file
	encryption = "privateKey" + change_ip_address(ip_ad)
	#loads the key paired with the sending computer
	module = __import__(encryption).decrypt
	#imports the decryption part of the key
	os.chdir(path)
	#goes to the file
	fileRead = open(filename, READ_BINARY_MODE).read()
	#loads file to this program
	os.chdir(current)
	#goes back to encryption programs to load and finish running programs
	module(fileRead,filename,path)
	#runs the decryption
if task =='k':
	ipAd= get_other_ip_ad()
	#needs the other address to connect via FTP and to label the key
	yourIpAd = input ('What is your ip address? ')
	#labels the public key
	n, e, d = gen_key()
	#generates the numbers needed
	filename1 = "privateKey" + change_ip_address(ipAd) + ".py"
	filename2 = "publicKey" + change_ip_address(yourIpAd) + ".py"
	#creates blank files with the correct names
	fileRead = open(filename, READ_MODE).read()
	
	
	
	write_to_skely(n, d, filename1)
	write_to_skely(n, e, filename2)
	#inserts the numbers to finish the skeleton version of the key
	ftp= ftp_login(ip_ad)
	#connects to ftp
	ftp_placing(ftp, filename2)
	#puts key in the other computer
	os.remove(filename2)
	#removes useless public key because you have the private key!!!
