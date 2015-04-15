#clase AdaptadorDaoAdm
#autor DanielHenao

from Entidades import Persona
import FachadaBD

class AdaptadorDaoAdm():
	
	def __init__(self):
		fachada=FachadaBD.FachadaBD()
		fachada.conectarBD()
		
	def insertarAdm(self, Persona):
		
		cur = cn.cursor()  
		cur.execute("INSERT INTO Persona")
		
	def consultarAdm(self,Persona):
		
		cur = cn.cursor()  
		cur.execute("SELECT * FROM Persona WHERE ID="+codigo)
	
	def consultarAdm(self,nombre):
		
		cur = cn.cursor()  
		cur.execute("SELECT * FROM Persona WHERE ID="+nombre)
		
	
	def borrarAdm(self, id_Persona):
		
		cur = cn.cursor()  
		cur.execute("UPDATE Persona SET acticvo=false WHERE ID="+id_persona)
		
	def actualizreAdm(self, id_Persona):
		cur = cn.cursor()  
		cur.execute("UPDATE Persona SET acticvo=false WHERE ID="+id_persona)
