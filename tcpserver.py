import socket
# in this file we are going to create a tcp server
# first we need to specify the ip addres by socket.afinet which means ipv4 and socket.sockstream specifies the 
# type of connection that is tcp

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# now we need to store the host and get it by gethostname method
host = socket.gethostname()
# then we will specify the port 
port = 445
# after this we will bind the serversocket with host and port using the bind function
serversocket.bind((host,port))
# after this we need to listen for the tcp client by adding the listener
# in the listen we need add parameter to specify how many connections should be listen at a time
serversocket.listen(3)

while True:
    clientsocket,address=serversocket.accept()
    # .accept() will accept the tcp connection from the client
    # after accepting we will convert the address in to a string indicating that the connection has been established with the client server 
    print("received connection from %s" % str(address))
    # then we have to create a message
    # we want to move to back thats why we are using \r and \n
    message="Thanks for connecting "+"\r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()