#class DaoPersona
#autor Daniel Henao
import Fachada.py

class DaoPersona():
	
	fachada= FachadaBD()
	fachada.conectarBD()
	
	def insertarPersona(self):
		
		cur = cn.cursor()  
		cur.execute("INSERT INTO Persona")
		
	def consultarPersona(self,id_persona):
		
		cur = cn.cursor()  
		cur.execute("SELECT * FROM Persona WHERE ID="+id_persona)
		
	
	def borrarPersona(self, id_persona):
		
		cur = cn.cursor()  
		cur.execute("UPDATE Persona SET acticvo=false WHERE ID="+id_persona)
		
		
	
