# Clase Persona
# Daniel Henao

class Persona():
	def __init__(self):
		pass
		
		
	def asignarNombre(self,nombre):
		self._nombre=nombre
		
	def asignarApellido(self, apellido):
		self._apellido=apellido
		
	def asignarTelefono(self,telefono):
		self._telefono=telefono
		
	def asignarDireccion(self, direccion):
		self._direccion=direccion
		
	def asignarEmail(self, email):
		self._email=email
		
	def asignarCiudad(self,ciudad):
		self._ciudad=ciudad
		
	def asignarID(self,id_):
		self._id_=id_
		
	def obtenerID(self):
		return self._id_
		
	def obtenerNombre(self):
		return self._nombre
	
	def obtenerApellido(self):
		return self._apellido
		
	def obtenerTelefono(self):
		return self._telefono
		
	def obtenerDireccion(self):
		return self:_direccion
		
	def obtenerEmail(self):
		return self._email
		
	def obtenerCiudad(self):
		return self._ciudad
