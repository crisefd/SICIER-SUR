#server.py
#Oscar Shaitan Tigreros

import socket
import sys
import imp
import os
from thread import *
path = os.path.abspath(os.path.dirname(__file__) + '/' + '.././Almacenamiento/Acceso/Fachada.py')
#print path
fachada = imp.load_source("Fachada", path)

HOST = socket.gethostbyname(socket.gethostname())   # Se designa la IP del server
PORT = 5315 # Se designa el puerto

class Servidor():
	
	
	def __init__(self):		
		#self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._fachada = fachada.Fachada()
		#print 'Socket created'
				
	def escuchar(self):	
		try:
			self.socket.bind((HOST, PORT))
		except socket.error as msg:
			print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
			sys.exit()
			 
		print 'Socket bind complete'
		
		#Inicia la escucha del server
		self.socket.listen(2)
		print 'Socket now listening'
		#Seguir escuchando al cliente
		while 1:
			
			conn, addr = self.socket.accept()
			print 'Connected with ' + addr[0] + ':' + str(addr[1])
			 
			#Inicia un nuevo hilo con primer argumento la funcion que se va a ejecutar, y de segundo la lista de argumentos de la funcion.
			start_new_thread(self.clientthread ,(conn,))
		 
		self.socket.close()

	def clientthread(self, conn):
		#Enviar Mensaje al cliente
		conn.send('Welcome to the server. Type the function and parameters\n') #solo toma strings
		 
		#ciclo infinito
		while True:
			 
			#Datos que envia el cliente
			data = conn.recv(1024)
			reply = 'OK...' + data
			if not data: 
				break
		 
			conn.sendall(reply)
		 
		
		conn.close()

	




Servidor()