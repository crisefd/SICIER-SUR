#Clase abstracta GeneradorCertificados

from abc import *
from reportlab.pdfgen import canvas

class GeneradorCertificados():
	__metaclass__ = ABCMeta

	
	def recibirTexto(self, texto):
		self._texto = texto

	@abstractmethod
	def generarPDF(self):
		pass


