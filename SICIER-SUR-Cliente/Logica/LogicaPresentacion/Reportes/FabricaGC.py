#Fabrica de Generadores de Certificados
import GeneradorCertificados
import GeneradorCertificadosExcelencia
import GeneradorCertificadosAsistencia 
import GeneradorCertificadosParticipacion

class FabricaGC():


	def fabricarGC(self, tipo):
		if tipo == "asistencia":
			return GeneradorCertificadosAsistencia.GeneradorCertificadosAsistencia()
		elif tipo == "participacion":
			return GeneradorCertificadosParticipacion.GeneradorCertificadosParticipacion()
		elif tipo == "excelencia":
			return GeneradorCertificadosExcelencia.GeneradorCertificadosExcelencia()