import imp
import os
import sys

try:
	path = os.path.abspath(os.path.dirname(__file__) + '/' + '.././Control/Controladores.py')
	controladores = imp.load_source("Controladores", path)
except IOError as err:
	path = os.path.abspath(os.path.dirname(__file__) + '.././Control/Controladores.py')
	print ">> ", path
	controladores = imp.load_source("Controladores", path)



class Fachada():
	def __init__(self):
		self.controlAdm = controladores.ControladorAdm()
		self.controlCoor = controladores.ControladorCoor()
		self.controlMT = controladores.ControladorMT()
		self.controlLT = controladores.ControladorLT()
		self.controlCurso = controladores.ControladorCurso()
		self.controlMatricula = controladores.ControladorMatricula()

#f = Fachada()
"""
f.controlAdm.insertarAdm(city="New York", email="mary.jane@example.com", 
						first_name="Mary", last_name="Jane", tel_num="444555", 
						is_active='t', id="1034", pass_="spidy" )	

f.controlAdm.actualizarAdm('1034', {'city':'Los Angeles', 'email':'mary.jane4@example.com'})

f.controlAdm.eliminarAdm('1034')

adm = f.controlAdm.consultarAdmID('1034')

sq = f.controlAdm.consultarAdmNombreCompleto('Mary', 'Jane')
for adm in sq:
	print adm.city

s =f.controlAdm.consultarAdmPassUsr('mary.jane@example.com', 'spidy')
print s.last_name"""
