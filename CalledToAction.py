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
if task == "e":
	filename = input('What file would you like to encrypt? ')
	path = input(PATH_ASK)
	encryption = "publicKey" + change_ip_address(ip_ad)
	module = __import__(encryption).encrypt
	os.chdir(path)
	fileRead = open(filename, READ_BINARY_MODE).read()
	os.chdir(CURRENT)
	module(filename, fileRead)
	ftp= ftp_login(ip_ad)
	ftp_placing (ftp, filename, fileRead)
	os.remove(filename)
if task == "d":
	filename = input('What file would you like to decrypt? ')
	ip_ad = get_other_ip_ad()
	path = input (PATH_ASK)
	encryption = "privateKey" + change_ip_address(ip_ad)
	module = __import__(encryption).decrypt
	os.chdir(path)
	fileRead = open(filename, READ_BINARY_MODE).read()
	os.chdir(current)
	module(fileRead,filename,path)
if task =='k':
	ipAd= get_other_ip_ad()
	yourIpAd = input ('What is your ip address? ')
	n, e, d = gen_key()
	filename1 = "privateKey" + change_ip_address(ipAd) + ".py"
	filename2 = "publicKey" + change_ip_address(yourIpAd) + ".py"
	fileRead = open(filename, READ_MODE).read()
	write_to_skely(n, d, filename1)
	write_to_skely(n, e, filename2)
	ftp= ftp_login(ip_ad)
	ftp_placing(ftp, filename2)
	os.remove(filename2)
