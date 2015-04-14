#clase Curso
#autor Daniel Henao

class Curso():
	
	def asignarDescripcion(self,descripcion):
		self.__descripcion=descripcion
		
	def asignarNombre(self, nombre):
		self.__nombre=nombre
		
	def asignarCodigo(self,codigo):
		self.__codigo=codigo
		
	def asignarCohorte(self, cohorte):
		self.__cohorte=cohorte
		
	def asignarActividades(self,actividades):
		self.__actividades=actividades
		
	def asignarFechaInicio(self,fechaINI):
		self.__fechaINI=fechaINI
		
	def asignarFechaFin(self, fechaFin):
		self.__fechaFin=fechaFin
	
	def obtenerDescripcion(self):
		return self.__descripcion
		
	def obtenerNombre(self):
		return self.__nombre
		
	def obtebnerID(self):
		return self.__id__
		
	def obtenerCohortes(self):
		return self.__cohorte
		
	def obtenerActividades(self):
		return self.__actividades
		
	def obtenerFechaINI(self):
		return self.__fechaINI
		
	def obtenerFechaFin(self):
		return self.__fechaFin
	 
