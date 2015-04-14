#Generador Certificados Excelencia
from reportlab.pdfgen import canvas
import GeneradorCertificados

class GeneradorCertificadosExcelencia(GeneradorCertificados.GeneradorCertificados):
	
	def generarPDF(self):
		c = canvas.Canvas("CertificadoExcelencia.pdf")
		tokens = self._texto.split("\n")
		i = 0;
		for tok in tokens:
			c.drawString(0, 700  - i, tok)
			i += 15
		c.showPage()
		c.save()