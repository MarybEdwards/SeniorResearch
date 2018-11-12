import sys
import subprocess
from subprocess import call
import Encrypt
from Encrypt import gen_key
import ftplib
from ftplib import FTP
import getpass
import os
ip_ad = input ('Who would you like to receive this key? \nPlease input the IP address ')
your_ip_ad = input ('What is your ip address? ')
n, e, d = gen_key()
ip_ad1 = ip_ad.replace (".", "!")
n = str(d)
your_ip_ad1 = your_ip_ad.replace(".", "!")
d = str(d)
e = str(e)
skely = open('skeleton.txt', 'r').read()
filename1 = "privateKey" + ip_ad1 + ".py"
filename2 = "publicKey" + your_ip_ad1 + ".py"
f1 = open(filename1, 'w+')
f1.write("n= " + n + "\ne= " + d + " \n" + skely)
f2 = open(filename2, 'w+')
f2.write("n= " + n + " \ne= " + e + "\n" +skely)
storing = "STOR " filename2
ftp = FTP(ip_ad)
f2 = open(filename2, 'fr')
ftp.login(input('input your username '), getpass.getpass('input your password '))
ftp.cwd('Encrypt')
ftp.storbinary(storing, f2)
os.remove(filename2)
