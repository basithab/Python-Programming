'''
NAME         Abdul Baasit
DATE         20th October 2020 
DESCRIPTION  setting up communication between client and server using sockets.
            the following code has the configuration to send receive data on a particular
            port from server.
-------------------------------------------------------------------------'''
#builtin-functions------------------------------------------------------
import platform
import socket
import random
#-----------------------------------------------------------------------
#code------------------------------------------------------------------
try:
    #---variable setup-----------------------------------------
    target_server= 'localhost'
    target_port = 10000
    #---set up for client connection to server------------------
    absocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("connection to server IP address:",target_server," and port: ",target_port)
    absocket.connect((target_server, target_port))
    #------set up for message to be sent------------------------------------------
    ab_message ="a_abdulbaasit is using device: " + socket.gethostname() + ' ' + platform.system() + ' ' 
    ab_message+= platform.release() + ' ' + platform.version()
    times = random.randint(2,7)#a random value is selected between 2 and 7 , the selected number of messages are sent
    print('Sending{0}:times{1}'.format(ab_message,times))
    ab_message *= times
    ab_message = ab_message.encode('UTF-8')
    absocket.sendall(ab_message)
    amount_received = 0
    amount_expected = len(ab_message)
    while amount_received < amount_expected:
        data = absocket.recv(16)
        amount_received += len(data)
        print("Amount of data received:",data)
except Exception as ex:
    pass
finally:
    print(input("Press enter to close the application"))
    absocket.close()
#----------------------end of code------------------------------------------------------