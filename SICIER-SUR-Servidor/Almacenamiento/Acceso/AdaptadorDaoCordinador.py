#clase AdaptadorDaoCordinador
#autor DanielHenao

from Entidades import Persona
import FachadaBD

class AdaptadorDaoCordinador():
	
	def __init__(self):
		fachada=FachadaBD.FachadaBD()
		fachada.conectarBD()
		
	def insertarCordinador(self, cordinador):
		
		cur = cn.cursor()  
		cur.execute("INSERT INTO Persona")
		
	def consultarCordiadorID(self,codigo):
		
		cur = cn.cursor()  
		cur.execute("SELECT * FROM Persona WHERE ID="+codigo)
	
	def consultarCordinador(self,nombre):
		
		cur = cn.cursor()  
		cur.execute("SELECT * FROM Persona WHERE ID="+nombre)
		
	
	def borrarCordinador(self, id_Persona):
		
		cur = cn.cursor()  
		cur.execute("UPDATE Persona SET acticvo=false WHERE ID="+id_persona)
		
	def actualizarCordinador(self, id_Persona):
		cur = cn.cursor()  
		cur.execute("UPDATE Persona SET acticvo=false WHERE ID="+id_persona)
				
