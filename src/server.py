#!/usr/bin/python
import morse as MorseBerry
import socket
print 'hola'
#Create the socket
s = socket.socket()
host = '127.0.0.1' ###Put here the address of your Raspberry
port = 4444
s.bind((host,port))

s.listen(10)
print "Server running at " + host + ":" + str(port)
while True:
	c, address = s.accept()
	print "Conexion started with ", address
	c.send('START')
	message=c.recv(1024)
	if message=='READY':
		print 'Partner ready to send'
		c.send('SEND')
	while True:
		message = c.recv(1024)
		if message == 'CLOSE':
			print 'Closing...'
			c.close()
			break
		elif message == 'PETITION':
			c.send("SEND")
		elif message[0]=='M': #es un mensaje
			MorseBerry.morseToLight(message[2:])
			print message[2:]
			c.send("RECEIVED")
	print 'Connection closed with ', address
#Before ending the server, clean up the pins
MorseBerry.clean()
