#Generador Certificado Asistencia
from reportlab.pdfgen import canvas
import GeneradorCertificados

class GeneradorCertificadosAsistencia(GeneradorCertificados.GeneradorCertificados):

	def generarPDF(self):
		c = canvas.Canvas("CertificadoAsistencia.pdf")
		tokens = self._texto.split("\n")
		i = 0;
		for tok in tokens:
			c.drawString(0, 700  - i, tok)
			i += 15
		c.showPage()
		c.save()