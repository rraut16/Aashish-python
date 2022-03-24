import getpass
import time
import paramiko

host="192.168.56.101"
port=22
user="root"
#password=getpass.getpass()
password="root"



ssh_client =paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname=host,port=port,username=user,password=password)

ftp_client=ssh_client.open_sftp()

ftp_client.get("/home/ashu/Desktop/dockerfile","/Users/admin/Desktop/Dockerfile")

print("file transfer done")