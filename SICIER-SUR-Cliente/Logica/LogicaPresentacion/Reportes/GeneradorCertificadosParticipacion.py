#Generador Certificados de Participacion
from reportlab.pdfgen import canvas
import GeneradorCertificados

class GeneradorCertificadosParticipacion(GeneradorCertificados):
	
	def generarPDF(self):
		c = canvas.Canvas("Certificado_Participacion")
		c.drawString(1000, 1000, self._texto)
		c.showPage()
		c.save()