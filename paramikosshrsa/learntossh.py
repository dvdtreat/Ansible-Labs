#!/usr/bin/python3

import os

import paramiko

def commandissue(command_to_issue, sshsession):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

def main():
    sshsession = paramiko.SSHClient()

mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh.id_rsa")

sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.session.connect(hostname="10.10.2.3", 
