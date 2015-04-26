import socket
import pickle
import sys  
import struct
import time

#main function
"""if __name__ == "__main__":

    if(len(sys.argv) < 2) :
        print 'Usage : python client.py hostname'
        sys.exit()

    host = sys.argv[1]
    port = 8888"""

HOST = ''
PORT = 5315

class ClienteSocket():

	def __init__(self):
		try:
			self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error:
			print 'Failed to create socket'
			sys.exit()

	def conectar(self):
		try:
			self._socket.connect((HOST, PORT))
		except socket.gaierror:
			print 'Hostname could not be resolved. Exiting'
			sys.exit()
		print 'Socket Connected to ' + host + ' on ip ' + remote_ip

	def desconectar(self):
		try:
			self_socket.close()
		except socket.error as ex:
			print 'Close socket failed'

	def enviarMensaje(self, **datos):
		try:
			datos_serializados = pickle.dumps(datos)
			self._socket.send(datos_serializados)
		except socket.error as ex1:
			print 'Send failed', ex1
		except Exception as ex2:
			print 'Serialize failed', ex2

	def recibirRespuesta(self):
		datos = None
		try:
			datos = pickle.loads(self_socket.recv(8192))
		except socket.error as ex:
			print "Recieve failed"
		return datos




