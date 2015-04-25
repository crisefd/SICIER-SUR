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
		with db.atomic():
			try:
				adm = Adm.create(**args)
				adm.save() # Falta validar insercion
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2
		
	def actualizarAdm(self, id_, **args):
		self._conectarBD()
		with db.atomic():
			try:
				q = Adm.update(**args).where(Adm.id==id_)
				q.execute() # Falta validar actualizacion
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2

	def eliminarAdm(self, id_):
		pass #Falta implementar borrado logico

	def leerAdm(self, id_):
		self._conectarBD()
		try:
			adm = adm.get(Adm.id == id_)
		except Exception as ex1:
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2

		return adm

class ControladorCoor(Controlador):
	def insertarCoor(self, **args):
		self._conectarBD()
		with db.atomic():
			try:
				coor = Coor.create(**args)
				coor.save() # Falta validar insercion
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2
		
	def actualizarCoor(self, id_, **args):
		self._conectarBD()
		with db.atomic():
			try:
				q = Coor.update(**args).where(Coor.id==id_)
				q.execute() # Falta validar actualizacion
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2

	def eliminarCoor(self, id_):
		pass #Falta implementar borrado logico

	def leerCoor(self, id_):
		self._conectarBD()
		try:
			#sq = Adm.select().where(id=id_)
			coor = Coor.get(Coor.id == id_)
		except Exception as ex1:
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2

		return coor


		
		