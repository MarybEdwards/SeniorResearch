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


task = input('What would you like to do? \nEncrypt a file (e), decrypt a file(d), or send a public key (k)? ')
if task == "e":
	filename = input('What file would you like to encrypt? ')
	ip_ad = input ('Where would you like to send this file? \nPlease input an IP address ')
	ip_ad1 = ip_ad.replace(".", "!")
	path = input('What was the path provided? ')
	encryption = "publicKey" + ip_ad1
	module = __import__(encryption).encrypt
	os.chdir(path)
	f = open(filename, 'r').read()
	os.chdir(current)
	module(filename, f)
	ftp = FTP(ip_ad)
	f = open(filename, 'rb')
	ftp.login(input('input your username '), getpass.getpass('input your password '))
	ftp.storbinary('STOR ' + filename, f)
	os.remove(filename)
if task == "d":
	filename = input('What file would you like to decrypt? ')
	ip_ad = input ('Who sent this file? \nPlease input an IP address')
	path = input ('What was the path provided? ')
	ip_ad1 = ip_ad.replace(".", "!")
	encryption = "privateKey" + ip_ad1
	module = __import__(encryption).decrypt
	current = os.getcwd()
	os.chdir(path)
	f = open(filename, 'rb').read()
	os.chdir(current)
	module(f,filename,path)
if task =='k':
	ipAd= get_other_ip_ad()
	yourIpAd = input ('What is your ip address? ')
	n, e, d = gen_key()
	filename1 = "privateKey" + change_ip_address(ipAd) + ".py"
	filename2 = "publicKey" + change_ip_address(yourIpAd) + ".py"
	write_to_skely(n, d, filename1)
	write_to_skely(n, e, filename2)
	ftp= ftp_login(ip_ad)
	ftp_placing(ftp, filename2)
	os.remove(filename2)
