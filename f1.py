import paramiko
import getpass
import time
import configparser


config = configparser.ConfigParser()
config.read("c://Users//admin//Documents//python//Study//paramiko//data.config") # a pre defined method to read config data. 
host=config['server1']['host']
port=config['server1']['port']
user=config['server1']['user']
password=config['server1']['password']
print(host,port,user,"\n")
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,port=port,username=user,password=password) #function to connect to host using host details


command_list =["uname -a","fdisk -l","uptime"]

def cmd_exec(cmd):
  
   stdin,stdout,stderr=ssh_client.exec_command(cmd) 
   x = str(stdout.read()).strip("'") # stripping ' marker from starting and end of output
   z =x[2:].split("\\n") # This is a list 
   print("command is :", cmd,"\n")
   for i in z:   #taking output from list z once at a time
       print(i)
   print("-"*100) # used to write a line - in output
    
for i in command_list:    # passing command to module to from list 
     cmd_exec(i)

