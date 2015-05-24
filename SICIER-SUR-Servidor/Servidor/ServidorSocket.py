#server.py
#Oscar Shaitan Tigreros

import socket
import sys
import pickle
import imp
import os
from thread import *
try:
	path = os.path.abspath(os.path.dirname(__file__) + '/' + '.././Almacenamiento/Acceso/Fachada.py')
	#print path
	fachada = imp.load_source("Fachada", path)
except IOError as err:
	path = os.path.abspath(os.path.dirname(__file__)  + '.././Almacenamiento/Acceso/Fachada.py')
	#print path
	fachada = imp.load_source("Fachada", path)

HOST = socket.gethostbyname(socket.gethostname())   # Se designa la IP del server
PORT = 5317 # Se designa el puerto

class ServidorSocket():
	
	
	def __init__(self):		
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._fachada = fachada.Fachada()
		#print 'Socket created'
				
	def escuchar(self):	
		try:
			self.socket.bind((HOST, PORT))
			print "Listen at host {0} with port {1}".format(HOST, PORT)
		except socket.error as msg:
			print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
			sys.exit()

		print 'Socket bind complete'
		
		#Inicia la escucha del server
		self.socket.listen(5)
		print 'Socket now listening'
		#Seguir escuchando al cliente
		while True:
			conn, addr = self.socket.accept()
			print 'Connected with ' + addr[0] + ':' + str(addr[1])
			#Inicia un nuevo hilo con primer argumento la funcion
			#que se va a ejecutar, y de segundo la lista de argumentos de la funcion.
			start_new_thread(self.clientthread ,(conn,))
		self.socket.close()

	def clientthread(self, conn):
		#Enviar Mensaje al cliente
		#print "Enviando saludo al cliente nuevo..."
		#conn.sendall('Welcome to the server. Type the function and parameters\n') #solo toma strings
		#ciclo infinito
		#i = 0
		while True:
			#Datos que envia el cliente
			d = conn.recv(81920)
			#print d
			#datos = pickle.loads(d)
			if d == 'EXIT':
				break

			elif d != '':
				datos = pickle.loads(d)
				#print 'datos recibidos ', datos
				respuesta = pickle.dumps(self.responder(datos))
				conn.send(respuesta)
		conn.close()

	def responder(self, datos):
		try:
			funcion = datos['funcion']
			parametros = datos['parametros']
			if funcion == 'consultarAdmPassUsr':
				usr = parametros['usr']
				pass_ = parametros['pass']
				return self._fachada.controlAdm.consultarAdmPassUsr(usr, pass_)
			elif funcion == "consultarCoorPassUsr":
				usr = parametros['usr']
				pass_ = parametros['pass']
				return self._fachada.controlCoor.consultarCoorPassUsr(usr, pass_)
				print "Falta implementar"
			elif funcion == "cosultarLTPassUsr":
				usr = parametros['usr']
				pass_ = parametros['pass']
				return self._fachada.controlLT.consultarLTPassUsr(usr, pass_)
			elif funcion == "consultarMTPassUsr":
				usr = parametros['usr']
				pass_ = parametros['pass']
				return self._fachada.controlMT.consultarMTPassUsr(usr, pass_)
			elif funcion == "insertarLT":
				id_LT = parametros['id']
				histAcad = parametros['academic_background']
				expLaboral = parametros['labor_experience']
				del parametros['academic_background']
				del parametros['labor_experience']
				r1 = self._fachada.controlLT.insertarLT(**parametros)
				r2 = ''; r3 = ''
				if r1 == 'ok':
					r2 = self._fachada.controlLT.insertarHistorialAcademicoLT(id_LT, histAcad)
					r3 = self._fachada.controlLT.insertarExperienciaLaboralLT(id_LT, expLaboral)
				if r2 == 'ok' and r3 == 'ok':
					return 'ok'
				else:
					return 'error'
			elif funcion == 'activarLT':
				ids = parametros['ids']
				return self._fachada.controlLT.activarLT(ids)
			elif funcion == 'insertarCurso':
				return self._fachada.controlCurso.insertarCurso(parametros)
			elif funcion == "insertarCursoActividad":
				return self._fachada.controlCurso.insertarCursoActividad(parametros)
			elif funcion == "insertarCursoCohorte":
				return self._fachada.controlCurso.insertarCursoCohorte(parametros)
		except Exception as ex:
			print "Error en responder..." , ex
			return 'error'

	




#if __name__  == "__main__":
s = ServidorSocket()
s.escuchar()

