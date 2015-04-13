#server.py
#Oscar Shaitan Tigreros

import socket
import sys




s = socket.socket()         # Create a socket object
HOST = socket.gethostname() # Get local machine name
PORT = 5312 				# Reserve a port for your service.
s.bind((HOST, PORT))        # Bind to the port
print 'WATING CONECCTION'
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()                # Close the connection
