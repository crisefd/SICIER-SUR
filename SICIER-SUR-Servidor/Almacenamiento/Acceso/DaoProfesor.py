#Dao Profesor
import os
from Entidades import Profesor
import FachadaBD 

class DaoProfesor():
	
	def __init__(self):
		fachada = FachadaBD.FachadaBD()
		fachada.conectarBD()
		
	def insertarProfesor(self, profesor):
		cur = fachada.cursor()
		sql_str = "INSERT INTO Profesor VALUES({0}, {1}, {2}. {3}, {4}, ""{5}, {6}, {7}, {8}, {9} );".format(profesor.obtenerNombre(), 
		              profesor.obtenerApellido, profesor.obtenerID(), profesor.obtenerTelefono(), profesor.obtenerDireccion(),
		              profesor.obtenerEmail(), profesor.obtenerCiudad(), profesor.obtenerExperienciaLaboral(), profesor.obtenerHistorialAcademico())
		cur.execute()
	
	def actualizarProfesor(self, profesor):
		cur = FachadaBD.FachadaBD()
		sql_str = "UPDATE Profesor SET Nombre = {0}, Apellido = {1}, id = {2}, telefono = {3}, direccion = {4}, direccion = {5}, email = {6}, experiencia_laboral = {7}, historial_laboral = {8} ;".format(profesor.obtenerNombre(), 
		              profesor.obtenerApellido, profesor.obtenerID(), profesor.obtenerTelefono(), profesor.obtenerDireccion(),
		              profesor.obtenerEmail(), profesor.obtenerCiudad(), profesor.obtenerExperienciaLaboral(), profesor.obtenerHistorialAcademico())
		cur.execute()
		
	def borrarProfesor(self, idProfesor):
		cur = fachada.cursor()
		sql_str = "UPDATE Profesor SET activo = 'false' WHERE id_profesor = {0}".format(idProfesor)
	
	def consultarProfesor(self):
		pass
		
		
		
		
