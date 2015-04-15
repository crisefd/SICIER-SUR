#class AdaptadorDaoLT
#autor Daniel Henao
import FachadaBD
from Entidades import Profesor

class AdaptadorDaoLT():
	
	
	def __init__(self):
		fachada= FachadaBD.FachadaBD()
		fachada.conectarBD()

	
	def insertarMT(self):
		
		cur = fachada.cursor()  
		cur.execute("INSERT INTO Persona")
		
	def consultarMT(self,id_persona):
		
		cur = fachada.cursor()  
		cur.execute("SELECT * FROM Persona WHERE ID="+id_persona)
		
	
	def borrarMT(self, id_persona):
		
		cur = fachada.cursor()  
		cur.execute("UPDATE Persona SET acticvo=false WHERE ID="+id_persona)
		
		
	
