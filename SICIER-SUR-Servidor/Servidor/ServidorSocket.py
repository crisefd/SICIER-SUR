#server.py
#Oscar Shaitan Tigreros

import socket
import sys
import pickle
import imp
import os
from thread import *
path = os.path.abspath(os.path.dirname(__file__) + '/' + '.././Almacenamiento/Acceso/Fachada.py')
#print path
fachada = imp.load_source("Fachada", path)

HOST = socket.gethostbyname(socket.gethostname())   # Se designa la IP del server
PORT = 5315 # Se designa el puerto

class ServidorSocket():
	
	
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
		while True:
			
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
			datos = pickle.loads(conn.recv(8192))
			respuesta = self.responder(datos)
			if not datos: 
				break
			conn.send(repuesta)
		 
		
		conn.close()

	def responder(self, datos):
		funcion = datos['funcion']
		parametros = datos['paramentros']
		if funcion == 'consultarAdmPassUsr':
			usr = parametros['usr']
			pass_ = parametros['pass']
			return self._fachada.controlAdm.consultarAdmPassUsr(usr, pass_)

	




Servidor()