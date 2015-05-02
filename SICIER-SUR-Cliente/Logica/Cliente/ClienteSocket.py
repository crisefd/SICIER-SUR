import socket
import pickle
import sys  
import struct
import time
from peewee import SelectQuery

#main function
"""if __name__ == "__main__":

    if(len(sys.argv) < 2) :
        print 'Usage : python client.py hostname'
        sys.exit()

    host = sys.argv[1]
    port = 8888"""

HOST = '127.0.1.1'
PORT = 5317

class ClienteSocket():

	def __init__(self):
		try:
			self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.hayConexion = False
		except socket.error:
			print 'Failed to create socket'
			sys.exit()

	def conectar(self):
		try:
			self._socket.connect((HOST, PORT))
		except socket.gaierror:
			print 'Hostname could not be resolved. Exiting'
			sys.exit()
		print "Socket Connected to  host {0} with port {1}".format(HOST, PORT)
		self.hayConexion = True

	def desconectar(self):
		try:
			self._socket.close()
			self.hayConexion = False
		except socket.error as ex:
			print 'Close socket failed'

	def enviarMensaje(self, datos):
		try:
			if type(datos) == type('a'):
				self._socket.send(datos)
			else:
				datos_serializados = pickle.dumps(datos)
				self._socket.send(datos_serializados)
		except socket.error as ex1:
			print 'Send failed', ex1
			self.hayConexion = False
			return 'error'
		except Exception as ex2:
			print 'Serialization failed', ex2
			return 'error'
		return 'ok'

	def recibirRespuesta(self):
		datos = None
		print "Recibiendo respuesta"
		try:
			d = self._socket.recv(81920)
			#print "Tipo Respuesta d ", type(d)
			if type(d) != type('a'):
				print "Serializando"
				datos = pickle.loads()
			else:
				datos = d
		except socket.error as ex1:
			print "Recieve failed ", ex1
			self.hayConexion = False
			self.desconectar()
			self.conectar()
		except Exception as ex2:
			print "Answer deserialization failed ", ex2
			return "" 
		return datos




