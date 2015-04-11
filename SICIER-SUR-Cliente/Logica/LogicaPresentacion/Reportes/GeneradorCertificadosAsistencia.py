#Generador Certificado Asistencia
from reportlab.pdfgen import canvas
import GeneradorCertificados

class GeneradorCertificadosAsistencia(GeneradorCertificados):


	def generarPDF(self):
		c = canvas.Canvas("Certificado_Asistencia")
		c.drawString(1000, 1000, self._texto)
		c.showPage()
		c.save()


