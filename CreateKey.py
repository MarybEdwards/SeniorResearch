import sys
import subprocess
from subprocess import call
import Math
from Math import gen_key
import FTPStuff
from FTPStuff import ftp_login
from FTPStuff import ftp_placing
from FTPStuff import get_other_ip_ad
import os


ipAd= get_other_ip_ad()
yourIpAd = input ('What is your ip address? ')
n, e, d = gen_key()
n = str(n)
d = str(d)
e = str(e)
filename1 = "privateKey" + change_ip_address(ipAd) + ".py"
filename2 = "publicKey" + change_ip_address(yourIpAd) + ".py"
write_to_skely(n, d, filename1)
write_to_skely(n, e, filename2)
ftp= ftp_login(ip_ad)
ftp_placing(ftp, filename2)
os.remove(filename2)
