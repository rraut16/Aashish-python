import getpass
import time
import paramiko
import re

host="192.168.56.2"
port=22
user="root"
#password=getpass.getpass()
password="root"



ssh_client =paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname=host,port=port,username=user,password=password)

stdin,stdout,stderr=ssh_client.exec_command("cd /;ls")
#command = ["cd ;/","df -kh"]

#stdin,stdout,stderr=ssh_client.exec_command(command)

#time.sleep(4)
x = stdout.readlines()
#print(stdout.read()) #tuple output 
for  i in x:
     print (i)
#   i = i.split()
 #   if 'on' in i:
  #      i.pop(-1)
   #     i[-1] = 'Mounted on'
    #print(' | '.join(i))


