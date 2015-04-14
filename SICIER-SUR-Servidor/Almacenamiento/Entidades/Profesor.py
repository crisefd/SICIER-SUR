#Profesor
import Persona


class Profesor(Persona.Persona):
	def __init__(self):
		pass
	
	def asignarHistorialAcademico(self, HA):
		self._historialAcademico = HA
	
	def asignarExperienciaLaboral(self, EL):
		self._experienciaLabora = EL
	
	def obtenerHistorialAcademico(self):
		return self._historialAcademico
	
	def obtenerExperienciaLaboral(self):
		return self._experienciaLaboral
		
