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
	all_client_connections.append(connection)
	print("Server connections: ", all_client_connections)
	# create a message to inform all other clients 
	# that a new client has just joined.
	broadcast_message = "New client joined: " + str(addr)
	# broadcast this message to the others
	broadcast(connection, broadcast_message)


	### Your code ends here ###

	while True:
		message = connection.recv(2048).decode()
		print (now() + " " +  str(addr) + "#  ", message)
		if (message == "exit" or not message):
			break
		### Write your code here ###
		#broadcast this message to the others
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
	for client in all_client_connections:
		if client != connection:
			client.send(message.encode())

	### Your code ends here ###

def main():
	"""
	creates a server socket, listens for new connections,
	and spawns a new thread whenever a new connection join
	"""
	serverPort = 12007
	serverName = "127.0.0.14"
	serverSocket = socket(AF_INET,SOCK_STREAM)
	try:
		# Use the bind function wisely!
		### Write your code here ###
		serverSocket.bind(('', serverPort))

		### Your code ends here ###
		
	except: 
		print("Bind failed. Error : ")
		sys.exit()
	serverSocket.listen(10)
	print ('The server is ready to receive')
	while True:
		### Write your code here ###
		connectionSocket, addr = serverSocket.accept()
		### You code ends here ###
		 
		print('Server connected by ', addr) 
		print('at ', now())
		thread.start_new_thread(handleClient, (connectionSocket,addr)) 
	serverSocket.close()

if __name__ == '__main__':
	main()
