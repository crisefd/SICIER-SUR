#class DaoPersona
#autor Daniel Henao
import FachadaBD
from Entidades import Persona

class DaoPersona():
	
	
	def __init__(self):
		fachada= FachadaBD.FachadaBD()
		fachada.conectarBD()

	
	def insertarPersona(self):
		
		cur = fachada.cursor()  
		cur.execute("INSERT INTO Persona")
		
	def consultarPersona(self,id_persona):
		
		cur = fachada.cursor()  
		cur.execute("SELECT * FROM Persona WHERE ID="+id_persona)
		
	
	def borrarPersona(self, id_persona):
		
		cur = fachada.cursor()  
		cur.execute("UPDATE Persona SET acticvo=false WHERE ID="+id_persona)
		
		
	
