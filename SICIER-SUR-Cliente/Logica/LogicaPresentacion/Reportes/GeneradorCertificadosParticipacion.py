#Generador Certificados de Participacion
from reportlab.pdfgen import canvas
import GeneradorCertificados

class GeneradorCertificadosParticipacion(GeneradorCertificados.GeneradorCertificados):
	
	def generarPDF(self):
		c = canvas.Canvas("CertificadoParticipacion.pdf")
		tokens = self._texto.split("\n")
		i = 0;
		for tok in tokens:
			c.drawString(0, 700  - i, tok)
			i += 15
		c.showPage()
		c.save()