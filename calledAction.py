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
  #calls for encrypting a file
  filename = input('What file would you like to encrypt? ')
  #requires the person to start in the directory in which the file is stored to get the path for the filename
  ip_ad = input ('Where would you like to send this file? \nPlease input an IP address ')
  ip_ad1 = ip_ad.replace(".", "!")
  path = input('What was the path provided? ')
  #the path provided was the shown due to the alias created in the system for people who are inept at dealing with computers
  encryption = "publicKey" + ip_ad1
  module = __import__(encryption).encrypt
  #this loads the file with the name saved through the ip address and the "def" of encryption
  current = os.getcwd()
  #so that the computer will be able to change directories to and from the file place and the encryption place
  os.chdir(path)
  f = open(filename, 'r').read()
  #reads the file while it is in that directory so it can go back the the directory with the code and finish doing stuff with it
  os.chdir(current)
  module(filename, f)
  #runs the encryption with the file
  ftp = FTP(ip_ad)
  f = open(filename, 'rb')
  ftp.login(input('input your username '), getpass.getpass('input your password '))
  ftp.storbinary('STOR ' + filename, f)
  os.remove(filename)
  #removes the new file that was just created on the computer as it was saved to the ftp file in the other computer
if what == "d":
  filename = input('What file would you like to decrypt? ')
  ip_ad = input ('Who sent this file? \nPlease input an IP address')
  #allows the computer to grab the correct key that corresponds to the other person
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