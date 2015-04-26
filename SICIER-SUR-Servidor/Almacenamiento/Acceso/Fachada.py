import imp
import os
import sys

path = os.path.abspath(os.path.dirname(__file__) + '/' + '.././Control/Controladores.py')
controladores = imp.load_source("Controladores", path)

ControladorAdm = controladores.ControladorAdm
ControladorCoor = controladores.ControladorCoor
ControladorMT = controladores.ControladorMT
ControladorLT = controladores.ControladorLT
ControladorCurso = controladores.ControladorCurso
ControladorMatricula = controladores.ControladorMatricula

class Fachada():
	def __init__(self):
		self.controlAdm = ControladorAdm.ControladorAdm()
		self.controlCoor = ControladorCoor.ControladorCoor()
		self.controlMT = ControladorMT.ControladorMT()
		self.controlLT = ControladorLT.ControladorLT()
		self.controlCurso = ControladorCurso.ControladorCurso()
		self.controlMatricula = ControladorMatricula.ControladorMatricula()
