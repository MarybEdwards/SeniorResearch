import subprocess
from subprocess import call
import ftplib
from ftplib import FTP
import sys
from sys import modules
import os
import getpass
what = input('What would you like to do? \nEncrypt a file (e), decrypt a file(d), or send a public key (s)? ')
if what == "e":
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
if what == "d":
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
if what =='s':
	module = __import__('createKey')
	module
