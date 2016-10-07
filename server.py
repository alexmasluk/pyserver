#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
serverPort = 12000
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end
    try:
        message = connectionSocket.recv(1024).decode()#Fill in start #Fill in end
        print(message)
        filename = message.split()[1]

        with open(filename[1:]) as f:
            outputdata = f.read()
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send(b"HTTP/1.1 200 OK\n\n");
        #Fill in end
        #Send the content of the requested file to the client
        outputdata = bytes(outputdata, 'UTF-8')
        print(outputdata)
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send(b"HTTP/1.1 404 Not Found\n\n");
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()
