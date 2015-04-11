#Generador Certificados de Participacion
from reportlab.pdfgen import canvas

class GeneradorCertificadosParticipacion(GeneradorCertificados):
	def generarPDF(self):
		c = canvas.Canvas("Certificado_Participacion")
		c.drawString(1000, 1000, self._texto)
		c.showPage()
		c.save()