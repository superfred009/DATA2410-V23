#Client side connects to the server and sends a message to everyone

import socket
import select
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# write server ip and port, and connect
### write your code here ###
serverName = "127.0.0.1"
serverPort = 12006

try:
	client_socket.connect((serverName,serverPort))
	print("Connected to server")
except:
	print("ConnectionError")
	sys.exit()

### your code ends here ###

while True:

	""" we are going to use a select-based approach here because it will help
	us deal with two inputs (user's input (stdin) and server's messages from socket)
	"""
	inputs = [sys.stdin, client_socket]

	""" read the select documentations - You pass select three lists: the 
	first contains all sockets that you might want to try reading; the 
	second all the sockets you might want to try writing to, and the last 
	(normally left empty) those that you want to check for errors. """

	read_sockets,write_socket, error_socket = select.select(inputs,[],[])

	
	# we check if the message is either coming from your terminal or 
	# from a server
	for socks in read_sockets:
		if socks == client_socket:

			# receive message from server and display it on the client side 
			# also handle exceptions here if there is no message from the 
			# client, you should exit.

			### write your code here ###

			message = socks.recv(2048).decode()
			print(message)

			### your code ends here ###

		else:
			#takes inputs from the user and print message
			#send a message to the server
			### write your code here ###

			sentence = input()
			print("You: " + sentence)
			client_socket.send(sentence.encode())
			if (sentence == "exit"):
				client_socket.close()

			### your code ends here ###

			
client_socket.close()
