'''
NAME         Abdul Baasit
DATE         20th October 2020 
DESCRIPTION  setting up communication between client and server using sockets.
            the following code has the configuration to send receive data on a particular
            port from server.
-------------------------------------------------------------------------'''
#builtin-functions------------------------------------------------------
import socket
#-----------------------------------------------------------------------
#Variables--------------------------------------------------------------
local_address = "0.0.0.0"
local_port = 10000
absocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Set up for server listening 
absocket.bind((local_address,local_port))
print("Server is listening to IP ",local_address,"on port",local_port)
absocket.listen(1)
#-------------------------------------------------------------------------
#code---------------------------------------------------------------------
while True:
    print("waiting for a connection")
    connection, client_address = absocket.accept()
    try:
        print("connecetion from IP address: ",client_address)
        while True:
            data = connection.recv(16)
            print("data received: ",data)
            if data:
                print("Data is being sent back to client")
                connection.sendall(data)
            else:
                print("no data from",client_address)
                break
    except Exception as ex:
        pass
    finally:
        connection.close()
#-------------------------------------------------------------------
