#Generador Certificados Excelencia
from reportlab.pdfgen import canvas
import GeneradorCertificados

class GeneradorCertificadosExcelencia(GeneradorCertificados):
	
	def generarPDF(self):
		c = canvas.Canvas("Certificado_Excelencia")
		c.drawString(1000, 1000, self._texto)
		c.showPage()
		c.save()