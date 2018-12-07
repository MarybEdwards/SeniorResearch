# SeniorResearch
My senior research project based on public key encryption written in python 3 in a linux os

First download all the encryption files and save them to one directory on each computer

Then set up ftp on both computers by:

	sudo apt-get install vsftpd
 	sudo apt-get install xinetd
	sudo apt-get install ftp
in 
	
	sudo nano /etc/vsftpd.conf 
change 
	
	listen = YES
	#local_enable=YES
	anonymous_enable=YES
	#write_enable=YES
to 
	 
	listen = NO
	local_enable=YES
	anonymous_enable=NO
	write_enable=YES	
In the file:
	
	sudo nano /etc/xinetd.d/vsftpd
write:
   
   	service ftp
        {
          disable                 = no
          socket_type             = stream
          wait                    = no
          user                    = thisComputersUserName
          server                  = /usr/sbin/vsftpd
          per_source              = 5
          instances               = 200
          banner_fail             = /etc/vsftpd.busy
          log_on_success          += PID HOST DURATION
          log_on_failure          += HOST
        }
exit to command line then type:	
				
  	sudo service vsftpd stop
  	sudo service vsftpd start
  	sudo add userNameOfOtherComputer
in the file :
	
	sudo nano /etc/passwd
Edit the line starting with the userNameOfOtherComputer to have parts matching line for the user on this computer so it resembles the following

	MyUserName:x:1000:1000:MyUserName,,,:/home/MyUserName:/bin/bash
	OtherUserName:x:1000:1001:OtherUserName,,,:/home/MyUserName:/bin/bash
Exit to command line, then type 
 
	sudo passwd userNameOfOtherComputer
  	passWordOfOtherComputer
	
in the file:
		
	sudo nano ~/.bashrc
write in 
   
	 alais encrypt = 'echo "your path is " ; pwd; cd / home/pathToEncryptionFile ; p$n2 calledAction.py; cd -'
Test to double check the ftp connection by typing:
	
	ftp ipAddressOfOtherComputer
	ThisCOmputer'sUsername
	ThisComputer'sPassword
It does not come up with an error then the connection is good and everything is set up and you are ready to test it!
If you have a specific directory you want all the files to be sent to do this:

	ftp ipAddressOfThisComputer
	ThisComputer'sUsername
	ThisComputer'sPassword
	lcd DirectorName
Before sending an encrypted file you need to send a key so send a key from each computer by typing in encrypt and following the directions
Then you can send a file by going to the directory where the file is stored and typing encrypt and following the directions
To decrypt a file just go to the directory in which it was saved and type encrypt and follow the directions.
