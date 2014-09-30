#!/usr/local/bin/python

import paramiko
from paramiko.ssh_exception import AuthenticationException

host1 = ['10.235.10.1', '10.235.10.2', '10.235.10.3', '10.235.10.4', '10.235.10.5',
         '10.235.10.6', '10.235.10.7', '10.235.10.8', '10.235.1.12', '10.235.2.12',
         '10.235.3.12', '10.235.4.12', '10.235.5.12', '10.235.6.12', '10.235.7.12', '10.235.8.12']

host2 = ['10.235.1.100', '10.235.2.100', '10.235.3.100', '10.235.4.100', '10.235.5.100',
         '10.235.6.100', '10.235.7.100', '10.235.8.100', '10.235.1.50', '10.235.2.50',
         '10.235.3.50', '10.235.4.50', '10.235.5.50', '10.235.6.50', '10.235.7.50', '10.235.8.50']

def printlines(out):
    for line in out.readlines():
        print line.rstript('\n')

def dropKey(host, username, password):
    try:
        ssh.connect(host, username=username, password=password)
        ssh.exec_command('mkdir -p ~/.ssh/')
        ssh.exec_command('echo "<inputsshkeyhere>" > ~/.ssh/authorized_keys')
        print "SSH Key dropped on %s" % host
        ssh.close()
    except AuthenticationException:
        print "Auth Error on %s" % host
        ssh.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for host in host1:
    dropKey(host, 'root', 'password')

for host in host2:
    dropKey(host, 'root', 'changeme')
