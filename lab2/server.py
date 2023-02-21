"""
Server side: it simultaneously handle multiple clients
and broadcast when a client new client joins or a client
sends a message.
"""
from socket import *
import _thread as thread
import time
import sys


#this is too keep all the newly joined connections! 
all_client_connections = []

def now():
	"""
	returns the time of day
	"""
	return time.ctime(time.time())

def handleClient(connection, addr):
	"""
	a client handler function 
	"""
	#this is where we broadcast everyone that a new client has joined
	
	### Write your code here ###
	# append this this to the list for broadcast

	# When a new client joins we append it to the connection list
	# The server also prints all connected client's address and port number
	# to keep track of all connected clients
	all_client_connections.append(connection)
	print("Server connections: ", all_client_connections)

	# create a message to inform all other clients 
	# that a new client has just joined.

	# We create a broadcast message that a client joins by adding the address to a "client joined" string
	broadcast_message = "New client joined: " + str(addr)
	# broadcast this message to the others using the broadcast function
	broadcast(connection, broadcast_message)


	### Your code ends here ###

	while True:
		message = connection.recv(2048).decode()
		print (now() + " " +  str(addr) + "#  ", message)
		if (message == "exit" or not message):
			break
		### Write your code here ###
		#broadcast this message to the others

		# Broadcast message is created by adding the address to the message
		# with the split method we remove the port number from the address to make it more readable
		broadcast_message = "From "+str(addr).split()[1] + ": " + message
		broadcast(connection, broadcast_message)
		
		### Your code ends here ###
	connection.close()
	all_client_connections.remove(connection)
	leave_message = "Client left: " + str(addr)
	broadcast(connection, leave_message)

def broadcast(connection, message):
	print ("Broadcasting")
	### Write your code here ###

	# Broadcast this message to the other clients
	# We loop through all the clients in the connection list
	# and send the message to all clients except the client that sent the message
	for client in all_client_connections:
		if client != connection:
			client.send(message.encode())

	### Your code ends here ###

def main():
	"""
	creates a server socket, listens for new connections,
	and spawns a new thread whenever a new connection join
	"""
	serverPort = 12008
	serverName = "127.0.0.14"
	serverSocket = socket(AF_INET,SOCK_STREAM)
	try:
		# Use the bind function wisely!
		### Write your code here ###
		# Bind the server to the serverName and serverPort
		# If the bind fails the server exits
		serverSocket.bind(('', serverPort))

		### Your code ends here ###
		
	except: 
		print("Bind failed. Error : ")
		sys.exit()
	serverSocket.listen(10)
	print ('The server is ready to receive')
	while True:
		### Write your code here ###

		# Accept the connection and print the address of the client
		connectionSocket, addr = serverSocket.accept()
		### You code ends here ###
		 
		print('Server connected by ', addr) 
		print('at ', now())
		thread.start_new_thread(handleClient, (connectionSocket,addr)) 
	serverSocket.close()

if __name__ == '__main__':
	main()
