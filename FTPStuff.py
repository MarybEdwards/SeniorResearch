import sys
import subprocess
from subprocess import call
import ftplib
from ftplib import FTP
import getpass
readBinaryMode = "'rb'"
def ftp_login (ipAdress):
        connection = FTP(ipAdress)
        connection.login(input('input your username '), getpass.getpass('input your password '))
        return connection

def ftp_placing (connection, filename, fileRead):
	fileRead = open(filename, readBinaryMode)
	if filename.find("publickey")>=(0):
		 ftp.cwd('Encrypt')	
        connection.storbinary('STOR '+filename, fileRead)

def get_other_ip_ad():
	ipAddress = input('what is the ip address of the other party in this transaction?')
	return ipAddress
