#clase DaoCurso
#autor DanielHenao

from Entidades import Curso
import FachadaBD

class DaoCurso():
	
	def __init__(self):
		fachada=FachadaBD.FachadaBD()
		fachada.conectarBD()
		
	def insertarCurso(self, curso):
		
		cur = cn.cursor()  
		cur.execute("INSERT INTO Persona")
		
	def consultarCursoCodigo(self,codigo):
		
		cur = cn.cursor()  
		cur.execute("SELECT * FROM Persona WHERE ID="+codigo)
	
	def consultarCurso(self,nombre):
		
		cur = cn.cursor()  
		cur.execute("SELECT * FROM Persona WHERE ID="+nombre)
		
	
	def borrarCurso(self, id_curso):
		
		cur = cn.cursor()  
		cur.execute("UPDATE Persona SET acticvo=false WHERE ID="+id_persona)
		
	def actualizaeCurso(self, curso):
		cur = cn.cursor()  
		cur.execute("UPDATE Persona SET acticvo=false WHERE ID="+id_persona)
				
