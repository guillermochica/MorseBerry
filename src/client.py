#!/usr/bin/python
import socket

#Create the socket
s = socket.socket()
destination_address = '192.168.1.7' ###Put here the address of your raspberry
destination_port = 4444
print "Connecting with ", destination_address
s.connect((destination_address,destination_port))
#send peticion de envio
received = s.recv(1024)
print received
while True:
	if received == 'START':
		s.send('READY')
		while True:
			received = s.recv(1024)
			if received =='SEND':
				message = raw_input('Write a message to send: ')
				s.send('M/'+message)
			elif received == 'RECEIVED':
				print 'The message has been received'
				while True:
					decision = raw_input('Do you want to send another message (Yes or No): ')
					if decision != 'Yes' and decision != 'No':
						print 'I do not understad that'
					else:
						break				
				if decision == 'Yes':
					print 'Sending petition...'
					s.send('PETITION')
				elif decision == 'No':
					print 'ADIOS'
					s.send('CLOSE')
					s.close()
					break
	break
