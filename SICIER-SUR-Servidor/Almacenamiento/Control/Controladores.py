# importe implicito de modelos, acceso total a Modelos.py

import sys
import imp
import os


path = os.path.abspath(os.path.dirname(__file__) + '/' + '.././Entidades/Modelos.py')
modelos = imp.load_source("Modelos", path)

bd = modelos.database
Adm = modelos.Administrator
Coor = modelos.Coordinator
MT = modelos.Masterteacher
LT = modelos.Leaderteacher



class Controlador():

	def _conectarBD(self):
		try:
			bd.connect()
		except Exception as err1:
			print err1
		
	def _desconectarBD(self):
		try:
			bd.close()
		except Exception as err2:
			print err2


class ControladorAdm(Controlador):
	
	def insertarAdm(self, **args):
		self._conectarBD()
		adm = Adm.create(id=args['id'], first_name=args['first_name'],
					last_name=args['last_name'], city=args['city'],
					tel_num=args['tel_num'], email=args['email'])
		n = adm.save()
		#Pendiente validacion de insercion
		