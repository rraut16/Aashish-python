#! /usr/bin/env python3
"""
  Title: Health_check_test.py
  Created on: 17th Feb 2021
  Author: Aashish Jangra.
  Python_Version: 3.5+
  Last Edited On: 28 July 2021

  ! Script Requirement:
    - yaml file which gives list of commands.
    - server config deatils in server config file
  * Change Log:
    -
  * Features:
    - script will take health check based on provided linux commands.
"""
import yaml
import paramiko
import time
import configparser




def run_command(cmd):
    """This function is to run command which is passed to this function."""
    host="192.168.56.101"
    port=22
    user="root"
    password="root"
    # Creating object for paramiko class.
    ssh_client =paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host,port=port,username=user,password=password)
    stdin,stdout,stderr=ssh_client.exec_command(cmd)
    j = stdout.readlines()
    with open("c://Users//admin//Documents//python//Study//paramiko//logs.txt", 'at') as f:
        f.write(cmd)  
        f.write("\n")  
        f.write("="*20)
        f.write("\n")
    for  i in j:
      with open("c://Users//admin//Documents//python//Study//paramiko//logs.txt", 'at') as f:
        f.write(i)  
    with open("c://Users//admin//Documents//python//Study//paramiko//logs.txt", 'at') as f:
        f.write("\n")
        f.write("#"*100)
        f.write("\n\n")


def get_cmds():
    with open("c://Users//admin//Documents//python//Study//paramiko//command_input.yaml", 'r') as f:
        user_data = yaml.safe_load(f)
    return user_data



def main():
    with open("c://Users//admin//Documents//python//Study//paramiko//logs.txt", 'w') as f:
      f.write(" ")  
    all_user_cmds = get_cmds()
    for command in all_user_cmds['COMMANDS']: # COMMAND is array of commands from command_input.yaml 
        run_command(command)
    

if __name__ == "__main__":
    main()  