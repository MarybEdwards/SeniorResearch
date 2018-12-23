import sys
import subprocess
from subprocess import call
import Math
from Encrypt import gen_key
import ftplib
from ftplib import FTP
import getpass
import os
ip_ad = input ('Who would you like to receive this key? \nPlease input the IP address ')
your_ip_ad = input ('What is your ip address? ')
n, e, d = gen_key()
ip_ad1 = ip_ad.replace (".", "!")
your_ip_ad1 = your_ip_ad.replace(".", "!")
n = str(n)
d = str(d)
e = str(e)
skely = open('skeleton.txt', 'r').read()
filename1 = "privateKey" + ip_ad1 + ".py"
filename2 = "publicKey" + your_ip_ad1 + ".py"
f1 = open(filename1, 'w+')
f1.write("n= " + n + "\ne= " + d + "\n" + skely)
f1.close()
f2 = open(filename2, 'w+')
f2.write("n= " + n + "\ne= " + e + "\n" +skely)
ftp = FTP(ip_ad)
f2 = open(filename2, 'rb')
ftp.login(input('input your username '), getpass.getpass('input your password '))
ftp.cwd('Encrypt')
ftp.storbinary('STOR ' + filename2, f2)
f2.close()
os.remove(filename2)
skely.close()
