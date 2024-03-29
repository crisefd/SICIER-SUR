import sys
import imp
import os

try:
	path = os.path.abspath(os.path.dirname(__file__) + '/' + '.././Entidades/Modelos.py')
	modelos = imp.load_source("Modelos", path)
except IOError as err:
	path = os.path.abspath(os.path.dirname(__file__)  + '.././Entidades/Modelos.py')
	modelos = imp.load_source("Modelos", path)

bd = modelos.database

Adm = modelos.Administrator
Coor = modelos.Coordinator
MT = modelos.Masterteacher
LT = modelos.Leaderteacher
LT_HA = modelos.LtAcademicBackg
MT_HA = modelos.MtAcademicBackg
LT_EL = modelos.LtLaborExp
MT_EL = modelos.MtLaborExp
Curso = modelos.Course
CursoAct = modelos.CourseActivity
ActNota = modelos.ActivityGrade
CursoCohorte = modelos.CourseCohort
Matricula = modelos.Enrollment



#Clase padre de los controladores
class Controlador():

	def _conectarBD(self):
		global bd
		try:
			bd.connect()
			#print "Conexion a la BD"
		except Exception as err1:
			print err1

		
	def _desconectarBD(self):
		global bd
		try:
			bd.close()
			#print "Desconexion de la BD"
		except Exception as err2:
			print err2


class ControladorAdm(Controlador):

	def insertarAdm(self, **datos):
		global bd
		self._conectarBD()
		try:
			adm = None
			with bd.atomic():
				adm = Adm.create(**datos)
			#print adm
			print adm.save() # Falta validar insercion
		except Exception as ex1:
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2
		
	def actualizarAdm(self, id_, datos):
		self._conectarBD()
		global bd
		try:
			q = None
			with bd.atomic():
				q = Adm.update(**datos).where(Adm.id==id_, Adm.is_active == True)
			q.execute() # Falta validar actualizacion
		except Exception as ex1:
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2

	def eliminarAdm(self, id_):
		self._conectarBD()
		global bd
		try:
			q = None
			with bd.atomic():
				q = Adm.update(is_active=False).where(Adm.id==id_)
			q.execute() # Falta validar actualizacion
		except Exception as ex1:
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2


	def consultarAdmID(self, id_):
		global bd
		self._conectarBD()
		try:
			adm = Adm.get(Adm.id == id_)
		except Exception as ex1:
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2

		return adm

	def consultarAdmPassUsr(self, usr, pass_):
		global bd
		self._conectarBD()
		sq = None
		try:
			sq = Adm.select().where(Adm.email == usr, 
				         Adm.pass_== pass_, Adm.is_active == True)
		except Exception as ex1:
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2
		it = sq.iterator()
		res = "1" #Si lo encontro
		try:
			it.next()
		except Exception as ex:
			res = "0" #No lo encontro

		return res

	def consultarAdmNombreCompleto(self, nombre, apellido):
		global bd
		self._conectarBD()
		sq = -1
		try:
			with bd.atomic():
				sq = Adm.select().where(Adm.first_name==nombre, Adm.last_name==apellido)
			#coor = Coor.get(Coor.id == id_)
		except Exception as ex1:
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2

		return sq

class ControladorCoor(Controlador):

	def insertarCoor(self, **datos):
		global bd
		self._conectarBD()
		try:
			with bd.atomic():
				coor = Coor.create(**datos)
			print coor.save() # Falta validar insercion
		except Exception as ex1:
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2
		
	def actualizarCoor(self, id_, datos):
		self._conectarBD()
		try:
			with bd.atomic():
				q = Coor.update(**datos).where(Coor.id==id_, Coor.is_active==True)
				q.execute() # Falta validar actualizacion
		except Exception as ex1:
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2

	def eliminarCoor(self, id_):
		self._conectarBD()
		global bd
		try:
			q = None
			with bd.atomic():
				q = Coor.update(is_active=False).where(Coor.id==id_, Coor.is_active==True)
			q.execute() # Falta validar actualizacion
		except Exception as ex1:
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2

	def consultarCoorID(self, id_):
		self._conectarBD()
		try:
			coor = Coor.get(Coor.id == id_)
		except Exception as ex1:
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2

		return coor

	def consultarCoorNombreCompleto(self, nombre, apellido):
		self._conectarBD()
		try:
			sq = Coor.get(Coor.first_name==nombre, Coor.last_name==apellido)
		except Exception as ex1:
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2

		return sq

class ControladorMT(Controlador):

	def insertarMT(self, **datos):
		self._conectarBD()
		with bd.atomic():
			try:
				mt = MT.create(**datos)
				mt.save() # Falta validar insercion
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2

	def insertarHistAcademicoMT(self, id_MT, historial):
		self._conectarBD()
		with bd.atomic():
			try:
				for item in historial:
					h = MT_HA.create(id=id_MT, item=item)
					h.save() #Falta validar insercion
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2

	def insertarExpLaboralMT(self, id_MT, experiencia):
		self._conectarBD()
		with bd.atomic():
			try:
				for item in experiencia:
					e = MT_EL.create(id=id_MT, item=item)
					e.save() #Falta validar insercion
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2



		def actualizarMT(self, id_MT, datos):
			self._conectarBD()
			with bd.atomic():
				try:
					q = MT.update(**datos).where(MT.id==id_MT)
					q.execute() # Falta validar actualizacion
				except Exception as ex1:
					print ex1
				finally:
					try:
						self._desconectarBD()
					except Exception as ex2:
						print ex2

		def eliminarMT(self, id_MT):
			pass #Falta implementar eliminado borrado logico

		def consultarMTID(self, id_MT):
			pass #Falta implementar consultas con join


class ControladorLT(Controlador):

	def insertarLT(self, **datos):
		global bd
		self._conectarBD()
		res = 'ok'
		try:
			lt = None
			with bd.atomic():
				lt = LT.create(**datos)
				n = lt.save()
				if n == 0:
					print "Insercion de LT fallida"
					res = 'error'
				else:
					print "Insercion de LT exitosa"
					res = 'ok'
		except Exception as ex1:
			res = 'error'
			print ex1
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print ex2
		return res

	def insertarHistorialAcademicoLT(self, id_LT, historial):
		self._conectarBD()
		global bd
		res = 'ok'
		try:
			print "Insertando hist acad ", historial
			for item in historial:
				print "Item hist ", item
				with bd.atomic():
					LT_HA.create(id_lt_fk=id_LT, item=item)
				#n = h.save()
				#if n == 0:
				#	print "historial ", item, "No pudo ser insertado"
				#	res = 'error'
				#	break
				#else:
				#	res = 'ok'
				#	print "Insercion de item historial academico exitosa"
		except Exception as ex1:
			res = 'error'
			print "1. ", type(ex1)
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print "2. ", type(ex2)
				print ex2
		return res

	def insertarExperienciaLaboralLT(self, id_LT, experiencia):
		self._conectarBD()
		res = 'ok'
		try:
			print "Insertado exp lab ", experiencia
			for item in experiencia:
				print "item exp: ", item
				with bd.atomic():
					LT_EL.create(id_lt_fk=id_LT, item=item)
				#n = e.save()
				#if n == 0:
				#	print "experiencia ", item, "No pudo ser insertada"
				#	res = 'error'
				#	break
				#else:
				#	res = 'ok'
				#	print "Insercion de experiencia existosa"
		except Exception as ex1:
			print "1", type(ex1)
			res = 'error'
		finally:
			try:
				self._desconectarBD()
			except Exception as ex2:
				print "2", type(ex2)
				res = 'error'
		return res



		def actualizarLT(self, id_LT, datos):
			self._conectarBD()
			with bd.atomic():
				try:
					q = LT.update(**datos).where(MT.id==id_LT)
					q.execute() # Falta validar actualizacion
				except Exception as ex1:
					print ex1
				finally:
					try:
						self._desconectarBD()
					except Exception as ex2:
						print ex2

		def eliminarLT(self, id_):
			pass #Falta implementar eliminado borrado logico

		def consultarLTID(self, id_MT):
			pass #Falta implementar consultas con join

class ControladorCurso(Controlador):

	def insertarCurso(self, **datos):
		self._conectarBD
		with bd.atomic():
			try:
				c = Curso.create(**datos)
				d.save()#Falta validar insercion
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2

	def insertarCursoActividades(self, id_curso, actividades):
		self._conectarBD
		with bd.atomic():
			try:
				for act in actividades:
					a = CursoAct.create(id_curso, act)
					a.save() #Falta validar insercion
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2

	def insertarCursoCohortes(self, id_curso, cohortes):
		self._conectarBD
		with bd.atomic():
			try:
				for cohorte in cohortes:
					a = CursoCohorte.create(id_curso, cohorte)
					a.save() #Falta validar insercion
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2

		def insertarActNota(self, **datos):
			self._conectarBD
			with bd.atomic():
				try:
					an = ActNota.create(**datos)
					an.save() #Falta validar insercion
				except Exception as ex1:
					print ex1
				finally:
					try:
						self._desconectarBD()
					except Exception as ex2:
						print ex2

		def actualizarActNota(self, id_, datos):
			self._conectarBD
			with bd.atomic():
				try:
					an = ActNota.update(**datos).where(ActNota.id == id_)
					an.execute() 
				except Exception as ex1:
					print ex1
				finally:
					try:
						self._desconectarBD()
					except Exception as ex2:
						print ex2

		def consultarActNota(self):
			pass #Falta implementar consulta de notas 

	
	
class ControladorMatricula(Controlador):

	def insertarMatricula(self, **datos):
		self._conectarBD
		with bd.atomic():
			try:
				c = Matricula.create(**datos)
				d.save()#Falta validar insercion
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2

	def actualizarMatricula(self, id_matricula, datos):
		self._conectarBD
		with bd.atomic():
			try:
				c = Matricula.update(**datos).where(Matricula.id == id_matricula)
				c.execute()
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2

	def consultarMatriculaID(self, id_):
		self._conectarBD
		sq = 0
		with bd.atomic():
			try:
				sq = Matricula.get(Matricula.id == id_)
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2
		return sq


	def consultarMatricula(self):
		self._conectarBD
		sq = 0
		with bd.atomic():
			try:
				sq = Matricula.select()
			except Exception as ex1:
				print ex1
			finally:
				try:
					self._desconectarBD()
				except Exception as ex2:
					print ex2
		return sq



#LT_HA.create(id_lt_fk='776', item='h1')

#c = ControladorLT()
#c.insertarExperienciaLaboralLT('776', ['e1', 'e2'])
#print sql.next()
		
