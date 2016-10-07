#!/usr/bin/python2
#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverPort = 12000
serverSocket.bind(('',serverPort))
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #from stackoverflow.com
serverSocket.listen(1)

while True:
    #Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    try:
        message = connectionSocket.recv(1024).decode()
        print(message)
        filename = message.split()[1]

        with open(filename[1:]) as f:
            outputdata = f.read()
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\n\n");
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\n\n");
        #Close client socket
        connectionSocket.close()
serverSocket.close()
