# Clase FachadaBD
# Daniel Henao

import psycop2, psycop2.extras

class FachadaBD():
	
	
	def conectarBD(self):
		cn = psycopg2.connect("host=localhost dbname=danielha user=danieha password=danielha")
		cur = cn.cursor()  
		cur.execute("SELECT campo1, campo2 FROM prueba")
		for fila in cur:
			campo1, campo2 = fila # extraer los campos
		print campo1, campo2
	


