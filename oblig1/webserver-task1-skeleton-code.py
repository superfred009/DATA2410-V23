#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket
#Write your code here

serverPort = 6969
serverName = "127.0.0.1337"
serverSocket = socket(AF_INET,SOCK_STREAM)

#End of your code
while True:
	#Establish the connection print('Ready to serve...') connectionSocket, addr = 
	try:
		#Write your code here

		#End of your code
		message = #Write your code here #End of your code 
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = #Write your code here #End of your code 

		#Send one HTTP header line into socket
		#Write your code here

		#End of your code

		#Send the content of the requested file to the client 
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode()) 
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()


	except IOError:
		#Send response message for file not found
    	#Write your code here

    	#End of your code
		
		#Close client socket
        
        #Write your code here
		
		#End of your code
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data