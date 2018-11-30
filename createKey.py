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
#n is shared between the two users but e is used only for the public key and d is used only for private keys
ip_ad1 = ip_ad.replace (".", "!")
your_ip_ad1 = your_ip_ad.replace(".", "!")
#done because the .'s would mess with the format of the file saved
n = str(n)
d = str(d)
e = str(e)
#done so they can be written into the public key and private key files when they are saved as .py files
skely = open('skeleton.txt', 'r').read()
#reading the text of the skeleton as a string, it includes all the programming needed for a key without the values
#that change per users 
filename1 = "privateKey" + ip_ad1 + ".py"
filename2 = "publicKey" + your_ip_ad1 + ".py"
#creates a file and includes which public/private key belongs to which pairing
f1 = open(filename1, 'w+')
f1.write("n= " + n + "\ne= " + d + "\n" + skely)
f1.close()
#adds the n value and d value into the key program
#the variable d is used despite it being labled e because they are used the same way in public and private keys making it easier
#to just have it be labled the same thing even with different numbers
#if someone has the d value, they can get the e value, so this has to stay private and not be sent
f2 = open(filename2, 'w+')
f2.write("n= " + n + "\ne= " + e + "\n" +skely)
#adds the n value and e value into the key program
#can probably get rid of above and fixed as below
ftp = FTP(ip_ad)
f2 = open(filename2, 'rb')
ftp.login(input('input your username '), getpass.getpass('input your password '))
#I set up the FTP to be based on the other computer but have a login for a user from the original computer... so this may not work on everyone's set up...
ftp.cwd('Encrypt')
ftp.storbinary('STOR ' + filename2, f2)
f2.close()
os.remove(filename2)
skely.close()
#removes the encrypted file once i
