#Clase ControladorCurso
#Autor Daniel Henao

from Acceso import DaoCurso
from Entidades import Curso

class ControladorCurso():
	
	def __init__():
		dao = DaoCurso.DaoCurso()
		
		
	
	def insertarCurso(self, **datos):
		descripcion = datos["descripcion"]
		nombre = datos["nombre"]
		codigo = datos["codigo"]
		cohortes = datos["cohortes"]
		
		actividades=datos["actividades"]
		fechaINI=datos["fechaINI"]
		fechaFin=datos["fechaFin"]
		
		curso= Curso.Curso()
		curso.asignarActividades(actividades)
		curso.asignarCodigo(codigo)
		curso.asignarCohorte(cohorte)
		curso.asignarDescripcion(descripcion)
		curso.asignarFechaFin(fechaFin)
		curso.asignarFechaInicio(fechaINI)
		curso.asignarNombre(nombre)
		dao.insertarCurso(curso)
		
	def borrarCurso(self, codigo):
		dao.borrarCurso(codigo)
		
	def consultarCurso(self,**datos):
		
		nombre=datos["nombre"]
		codigo=datos["codigo"]
		if nombre=="":
			dao.consultarCursoCodigo(codigo)
		else:
			dao.consultarCurso(nombre)
		
	
	
		
		 
		
		
		
