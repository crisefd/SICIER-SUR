## -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login-IGU.ui'
#
# Created: Sun Apr 26 09:51:56 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

import sys
from thread import *
import imp
import os
clientesocket = None

try:
	ss = os.path.dirname(__file__) + '/' + '../..'
	path = os.path.abspath(ss + '/..' + '/Logica/Cliente/ClienteSocket.py') 
	#print path
	clientesocket = imp.load_source("ClienteSocket", path)
except IOError as err:
	ss = os.path.dirname(__file__)  + '../..'
	path = os.path.abspath(ss + '/..' + '/Logica/Cliente/ClienteSocket.py') 
	clientesocket = imp.load_source("ClienteSocket", path)

clienteSocket = clientesocket.ClienteSocket()

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class VentanaRegistroAdm(QtGui.QFrame):
    def __init__(self):
        super(VentanaRegistroAdm, self).__init__()
        self.setupUi(self)

    def setupUi(self, VentanaRegistroAdm):
        VentanaRegistroAdm.setObjectName(_fromUtf8("VentanaRegistroAdm"))
        VentanaRegistroAdm.resize(733, 533)
        VentanaRegistroAdm.setFrameShape(QtGui.QFrame.StyledPanel)
        VentanaRegistroAdm.setFrameShadow(QtGui.QFrame.Raised)
        self.etiquetaTitulo = QtGui.QLabel(VentanaRegistroAdm)
        self.etiquetaTitulo.setGeometry(QtCore.QRect(110, 20, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitulo.setFont(font)
        self.etiquetaTitulo.setObjectName(_fromUtf8("etiquetaTitulo"))
        self.etiquetaSubTit = QtGui.QLabel(VentanaRegistroAdm)
        self.etiquetaSubTit.setGeometry(QtCore.QRect(260, 60, 101, 17))
        self.etiquetaSubTit.setStyleSheet(_fromUtf8("color: rgb(255, 55, 29);"))
        self.etiquetaSubTit.setObjectName(_fromUtf8("etiquetaSubTit"))
        self.etiquetaNombre = QtGui.QLabel(VentanaRegistroAdm)
        self.etiquetaNombre.setGeometry(QtCore.QRect(50, 100, 91, 17))
        self.etiquetaNombre.setObjectName(_fromUtf8("etiquetaNombre"))
        self.etiquetaApellido = QtGui.QLabel(VentanaRegistroAdm)
        self.etiquetaApellido.setGeometry(QtCore.QRect(380, 100, 91, 17))
        self.etiquetaApellido.setObjectName(_fromUtf8("etiquetaApellido"))
        self.etiquetaID = QtGui.QLabel(VentanaRegistroAdm)
        self.etiquetaID.setGeometry(QtCore.QRect(50, 200, 211, 17))
        self.etiquetaID.setObjectName(_fromUtf8("etiquetaID"))
        self.etiquetaCorreo = QtGui.QLabel(VentanaRegistroAdm)
        self.etiquetaCorreo.setGeometry(QtCore.QRect(50, 380, 66, 17))
        self.etiquetaCorreo.setObjectName(_fromUtf8("etiquetaCorreo"))
        self.etiquetaTel = QtGui.QLabel(VentanaRegistroAdm)
        self.etiquetaTel.setGeometry(QtCore.QRect(390, 300, 81, 17))
        self.etiquetaTel.setObjectName(_fromUtf8("etiquetaTel"))
        self.etiquetaDir = QtGui.QLabel(VentanaRegistroAdm)
        self.etiquetaDir.setGeometry(QtCore.QRect(50, 300, 81, 17))
        self.etiquetaDir.setObjectName(_fromUtf8("etiquetaDir"))
        self.etiquetaCiudad = QtGui.QLabel(VentanaRegistroAdm)
        self.etiquetaCiudad.setGeometry(QtCore.QRect(380, 200, 191, 17))
        self.etiquetaCiudad.setObjectName(_fromUtf8("etiquetaCiudad"))
        self.campoNombres = QtGui.QLineEdit(VentanaRegistroAdm)
        self.campoNombres.setGeometry(QtCore.QRect(30, 130, 301, 27))
        self.campoNombres.setObjectName(_fromUtf8("campoNombres"))
        self.campoApellidos = QtGui.QLineEdit(VentanaRegistroAdm)
        self.campoApellidos.setGeometry(QtCore.QRect(370, 130, 301, 27))
        self.campoApellidos.setObjectName(_fromUtf8("campoApellidos"))
        self.campoID = QtGui.QLineEdit(VentanaRegistroAdm)
        self.campoID.setGeometry(QtCore.QRect(30, 230, 301, 27))
        self.campoID.setObjectName(_fromUtf8("campoID"))
        self.campoCiudad = QtGui.QLineEdit(VentanaRegistroAdm)
        self.campoCiudad.setGeometry(QtCore.QRect(370, 230, 301, 27))
        self.campoCiudad.setObjectName(_fromUtf8("campoCiudad"))
        self.campoDir = QtGui.QLineEdit(VentanaRegistroAdm)
        self.campoDir.setGeometry(QtCore.QRect(30, 330, 301, 27))
        self.campoDir.setObjectName(_fromUtf8("campoDir"))
        self.campoTel = QtGui.QLineEdit(VentanaRegistroAdm)
        self.campoTel.setGeometry(QtCore.QRect(370, 330, 301, 27))
        self.campoTel.setObjectName(_fromUtf8("campoTel"))
        self.campoCorreo = QtGui.QLineEdit(VentanaRegistroAdm)
        self.campoCorreo.setGeometry(QtCore.QRect(30, 410, 301, 27))
        self.campoCorreo.setObjectName(_fromUtf8("campoCorreo"))
        self.botonAtras = QtGui.QPushButton(VentanaRegistroAdm)
        self.botonAtras.setGeometry(QtCore.QRect(160, 480, 98, 27))
        self.botonAtras.setObjectName(_fromUtf8("botonAtras"))
        self.botonEnviar = QtGui.QPushButton(VentanaRegistroAdm)
        self.botonEnviar.setGeometry(QtCore.QRect(360, 480, 98, 27))
        self.botonEnviar.setObjectName(_fromUtf8("botonEnviar"))

        self.retranslateUi(VentanaRegistroAdm)
        QtCore.QObject.connect(self.botonEnviar, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregarAdm)
        QtCore.QMetaObject.connectSlotsByName(VentanaRegistroAdm)
    
    def agregarAdm(self):
		global clienteSocket
		nombre = str(self.campoNombres.text())
		if nombre == '':
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("El campo nombre no puede estar vacio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			return
		apellido = str(self.campoApellidos.text())
		if apellido == '':
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("El campo apellido no puede estar vacio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			return
		id_ = str(self.campoID.text())
		if id_ == '':
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("El campo ID no puede estar vacio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			return
		ciudad = str(self.campoCiudad.text())
		if ciudad == '':
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("El campo ciudad no puede estar vacio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			return
		direccion = str(self.campoDir.text())
		if direccion == '':
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("El campo direccion no puede estar vacio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			return
		tel = str(self.campoTel.text())
		if tel == '':
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("El campo telefono no puede estar vacio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			return
		correo = str(self.campoCorreo.text())
		if correo == '':
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("El campo correo no puede estar vacio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			return
		datos = {'funcion': 'insertarAdm', 
				'parametros':{'first_name':nombre,'last_name':apellido,
				'id':id_, 'city':ciudad, 'tel_num':tel, 'email':correo,
				'is_active':True, 'pass_':nombre[0]+id_+apellido[0]
				}}
		clienteSocket.enviarMensaje(datos)
		res = clienteSocket.recibirRespuesta(False)
		if 'ok' in res:
			msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("El usuario fue ingresado correctamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
		elif 'error' in res:
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("El usuario no fue igresado correctamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

    def retranslateUi(self, VentanaRegistroAdm):
        VentanaRegistroAdm.setWindowTitle(_translate("VentanaRegistroAdm", "Frame", None))
        self.etiquetaTitulo.setText(_translate("VentanaRegistroAdm", "Registro de Administradores de CIER-SUR", None))
        self.etiquetaSubTit.setText(_translate("VentanaRegistroAdm", "(*)Obligatorio", None))
        self.etiquetaNombre.setText(_translate("VentanaRegistroAdm", "Nombres *", None))
        self.etiquetaApellido.setText(_translate("VentanaRegistroAdm", "Apellidos *", None))
        self.etiquetaID.setText(_translate("VentanaRegistroAdm", "Número de Documento de ID *", None))
        self.etiquetaCorreo.setText(_translate("VentanaRegistroAdm", "Correo *", None))
        self.etiquetaTel.setText(_translate("VentanaRegistroAdm", "Teléfono *", None))
        self.etiquetaDir.setText(_translate("VentanaRegistroAdm", "Dirección *", None))
        self.etiquetaCiudad.setText(_translate("VentanaRegistroAdm", " Municipio de residencia *", None))
        self.botonAtras.setText(_translate("VentanaRegistroAdm", "Atras", None))
        self.botonEnviar.setText(_translate("VentanaRegistroAdm", "Enviar", None))

class VentanaOpcionesRegistroCoor(QtGui.QFrame):
    def __init__(self):
        super(VentanaOpcionesRegistroCoor, self).__init__()
        self.ventanaRegMT = VentanaRegistroMT()
        self.setupUi(self)

    def setupUi(self, VentanaOpcionesRegistroCoor):
        VentanaOpcionesRegistroCoor.setObjectName(_fromUtf8("VentanaOpcionesRegistroCoor"))
        VentanaOpcionesRegistroCoor.resize(297, 217)
        VentanaOpcionesRegistroCoor.setFrameShape(QtGui.QFrame.StyledPanel)
        VentanaOpcionesRegistroCoor.setFrameShadow(QtGui.QFrame.Raised)
        self.label = QtGui.QLabel(VentanaOpcionesRegistroCoor)
        self.label.setGeometry(QtCore.QRect(40, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.botonMT = QtGui.QPushButton(VentanaOpcionesRegistroCoor)
        self.botonMT.setGeometry(QtCore.QRect(90, 80, 100, 27))
        self.botonMT.setObjectName(_fromUtf8("botonMT"))
        self.botonCoor = QtGui.QPushButton(VentanaOpcionesRegistroCoor)
        self.botonCoor.setGeometry(QtCore.QRect(90, 150, 100, 27))
        self.botonCoor.setObjectName(_fromUtf8("botonCoor"))

        self.retranslateUi(VentanaOpcionesRegistroCoor)
        QtCore.QMetaObject.connectSlotsByName(VentanaOpcionesRegistroCoor)
        QtCore.QObject.connect(self.botonMT, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaOpcionesRegistroCoor.mostrarVentanaRegMT)

    def mostrarVentanaRegMT(self):
        self.ventanaRegMT.show()

    def retranslateUi(self, VentanaOpcionesRegistroCoor):
        VentanaOpcionesRegistroCoor.setWindowTitle(_translate("VentanaOpcionesRegistroCoor", "Frame", None))
        self.label.setText(_translate("VentanaOpcionesRegistroCoor", "Registrar  Usuario", None))
        self.botonMT.setText(_translate("VentanaOpcionesRegistroCoor", "MasterTeacher", None))
        self.botonCoor.setText(_translate("VentanaOpcionesRegistroCoor", "Coordinator", None))

class VentanaOpcionesRegistroAdm(QtGui.QFrame):
	def __init__(self):
		super(VentanaOpcionesRegistroAdm, self).__init__()
		self.ventanaRegAdm = VentanaRegistroAdm()
		self.setupUi(self)

	def mostrarVentanaRegAdm(self):
		self.ventanaRegAdm.show()

	def setupUi(self, VentanaOpcionesRegistroAdm):
		VentanaOpcionesRegistroAdm.setObjectName(_fromUtf8("VentanaOpcionesRegistroAdm"))
		VentanaOpcionesRegistroAdm.resize(297, 217)
		VentanaOpcionesRegistroAdm.setFrameShape(QtGui.QFrame.StyledPanel)
		VentanaOpcionesRegistroAdm.setFrameShadow(QtGui.QFrame.Raised)
		self.label = QtGui.QLabel(VentanaOpcionesRegistroAdm)
		self.label.setGeometry(QtCore.QRect(40, 30, 221, 31))
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName(_fromUtf8("label"))
		self.botonAdm = QtGui.QPushButton(VentanaOpcionesRegistroAdm)
		self.botonAdm.setGeometry(QtCore.QRect(90, 80, 100, 27))
		self.botonAdm.setObjectName(_fromUtf8("pushButton"))
		self.botonCoor = QtGui.QPushButton(VentanaOpcionesRegistroAdm)
		self.botonCoor.setGeometry(QtCore.QRect(90, 150, 100, 27))
		self.botonCoor.setObjectName(_fromUtf8("pushButton_2"))

		self.retranslateUi(VentanaOpcionesRegistroAdm)
		QtCore.QObject.connect(self.botonAdm, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaOpcionesRegistroAdm.mostrarVentanaRegAdm)
		QtCore.QMetaObject.connectSlotsByName(VentanaOpcionesRegistroAdm)



	def retranslateUi(self, VentanaOpcionesRegistroAdm):
		VentanaOpcionesRegistroAdm.setWindowTitle(_translate("VentanaOpcionesRegistroAdm", "Frame", None))
		self.label.setText(_translate("VentanaOpcionesRegistroAdm", "Registrar  Usuario", None))
		self.botonAdm.setText(_translate("VentanaOpcionesRegistroAdm", "Administrator", None))
		self.botonCoor.setText(_translate("VentanaOpcionesRegistroAdm", "Coordinator", None))

class VentanaAsignarNotas(QtGui.QFrame):
    def __init__(self):
        super(VentanaAsignarNotas, self).__init__()
        self.setupUi(self)

    def setupUi(self, VentanaAsignarNotas):
        VentanaAsignarNotas.setObjectName(_fromUtf8("VentanaAsignarNotas"))
        VentanaAsignarNotas.resize(601, 577)
        self.etiquetaTitulo_2 = QtGui.QLabel(VentanaAsignarNotas)
        self.etiquetaTitulo_2.setGeometry(QtCore.QRect(240, 0, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitulo_2.setFont(font)
        self.etiquetaTitulo_2.setObjectName(_fromUtf8("etiquetaTitulo_2"))
        self.tabWidget = QtGui.QTabWidget(VentanaAsignarNotas)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 591, 441))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.campoBusqueda = QtGui.QLineEdit(self.tab_2)
        self.campoBusqueda.setGeometry(QtCore.QRect(260, 20, 301, 29))
        self.campoBusqueda.setObjectName(_fromUtf8("campoBusqueda"))
        self.botonBuscar = QtGui.QPushButton(self.tab_2)
        self.botonBuscar.setGeometry(QtCore.QRect(240, 180, 100, 27))
        self.botonBuscar.setObjectName(_fromUtf8("botonBuscar"))
        self.comboAtributos = QtGui.QComboBox(self.tab_2)
        self.comboAtributos.setGeometry(QtCore.QRect(130, 20, 91, 25))
        self.comboAtributos.setObjectName(_fromUtf8("comboAtributos"))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.tableWidget = QtGui.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 531, 101))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.etiquetaBuscar = QtGui.QLabel(self.tab_2)
        self.etiquetaBuscar.setGeometry(QtCore.QRect(35, 20, 81, 20))
        self.etiquetaBuscar.setObjectName(_fromUtf8("etiquetaBuscar"))
        self.campoIDActualizar_3 = QtGui.QLineEdit(self.tab_2)
        self.campoIDActualizar_3.setGeometry(QtCore.QRect(260, 210, 301, 29))
        self.campoIDActualizar_3.setText(_fromUtf8(""))
        self.campoIDActualizar_3.setObjectName(_fromUtf8("campoIDActualizar_3"))
        self.etiquetaIDActualizar_2 = QtGui.QLabel(self.tab_2)
        self.etiquetaIDActualizar_2.setGeometry(QtCore.QRect(30, 220, 191, 17))
        self.etiquetaIDActualizar_2.setObjectName(_fromUtf8("etiquetaIDActualizar_2"))
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 250, 531, 101))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.botonBuscar_2 = QtGui.QPushButton(self.tab_2)
        self.botonBuscar_2.setGeometry(QtCore.QRect(240, 360, 100, 27))
        self.botonBuscar_2.setObjectName(_fromUtf8("botonBuscar_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.etiquetaIDActualizar = QtGui.QLabel(self.tab)
        self.etiquetaIDActualizar.setGeometry(QtCore.QRect(10, 40, 191, 17))
        self.etiquetaIDActualizar.setObjectName(_fromUtf8("etiquetaIDActualizar"))
        self.campoIDActualizar = QtGui.QLineEdit(self.tab)
        self.campoIDActualizar.setGeometry(QtCore.QRect(220, 30, 311, 29))
        self.campoIDActualizar.setObjectName(_fromUtf8("campoIDActualizar"))
        self.campoIDActualizar_2 = QtGui.QLineEdit(self.tab)
        self.campoIDActualizar_2.setGeometry(QtCore.QRect(220, 90, 311, 29))
        self.campoIDActualizar_2.setObjectName(_fromUtf8("campoIDActualizar_2"))
        self.etiquetaIDActualizar_3 = QtGui.QLabel(self.tab)
        self.etiquetaIDActualizar_3.setGeometry(QtCore.QRect(10, 100, 191, 17))
        self.etiquetaIDActualizar_3.setObjectName(_fromUtf8("etiquetaIDActualizar_3"))
        self.etiquetaIDActualizar_4 = QtGui.QLabel(self.tab)
        self.etiquetaIDActualizar_4.setGeometry(QtCore.QRect(10, 140, 191, 17))
        self.etiquetaIDActualizar_4.setObjectName(_fromUtf8("etiquetaIDActualizar_4"))
        self.campoIDActualizar_4 = QtGui.QLineEdit(self.tab)
        self.campoIDActualizar_4.setGeometry(QtCore.QRect(220, 140, 61, 29))
        self.campoIDActualizar_4.setObjectName(_fromUtf8("campoIDActualizar_4"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 210, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.pushButton = QtGui.QPushButton(VentanaAsignarNotas)
        self.pushButton.setGeometry(QtCore.QRect(240, 520, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(VentanaAsignarNotas)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(VentanaAsignarNotas)

    def retranslateUi(self, ventana):
        ventana.setWindowTitle(_translate("ventana", "Dialog", None))
        self.etiquetaTitulo_2.setText(_translate("ventana", "CIER-SUR", None))
        self.botonBuscar.setText(_translate("ventana", "Buscar", None))
        self.comboAtributos.setItemText(0, _translate("ventana", "Nombre", None))
        self.comboAtributos.setItemText(1, _translate("ventana", "Apellido", None))
        self.comboAtributos.setItemText(2, _translate("ventana", "ID", None))
        self.comboAtributos.setItemText(3, _translate("ventana", "Correo", None))
        self.comboAtributos.setItemText(4, _translate("ventana", "Ciudad", None))
        self.etiquetaBuscar.setText(_translate("ventana", "Buscar por:", None))
        self.etiquetaIDActualizar_2.setText(_translate("ventana", "Actualizar Notas al LT con ID", None))
        self.botonBuscar_2.setText(_translate("ventana", "Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ventana", "Buscar LT", None))
        self.tab.setToolTip(_translate("ventana", "<html><head/><body><p><br/></p></body></html>", None))
        self.etiquetaIDActualizar.setText(_translate("ventana", "Actualizar Notas al LT con ID", None))
        self.etiquetaIDActualizar_3.setText(_translate("ventana", "Actividad con ID", None))
        self.etiquetaIDActualizar_4.setText(_translate("ventana", "Nota", None))
        self.pushButton_2.setText(_translate("ventana", "Actializar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ventana", "Actualizar Notas", None))
        self.pushButton.setText(_translate("ventana", "Cancelar", None))

class VentanaRevisarNotas(QtGui.QFrame):
    def __init__(self):
        super(VentanaRevisarNotas, self).__init__()
        self.setupUi(self)


    def setupUi(self, ventana):
        ventana.setObjectName(_fromUtf8("ventana"))
        ventana.resize(601, 577)
        self.etiquetaTitulo_2 = QtGui.QLabel(ventana)
        self.etiquetaTitulo_2.setGeometry(QtCore.QRect(240, 0, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitulo_2.setFont(font)
        self.etiquetaTitulo_2.setObjectName(_fromUtf8("etiquetaTitulo_2"))
        self.tabWidget = QtGui.QTabWidget(ventana)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 591, 441))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.campoBusqueda = QtGui.QLineEdit(self.tab_2)
        self.campoBusqueda.setGeometry(QtCore.QRect(260, 20, 301, 29))
        self.campoBusqueda.setObjectName(_fromUtf8("campoBusqueda"))
        self.botonBuscar = QtGui.QPushButton(self.tab_2)
        self.botonBuscar.setGeometry(QtCore.QRect(240, 180, 100, 27))
        self.botonBuscar.setObjectName(_fromUtf8("botonBuscar"))
        self.comboAtributos = QtGui.QComboBox(self.tab_2)
        self.comboAtributos.setGeometry(QtCore.QRect(100, 20, 151, 25))
        self.comboAtributos.setObjectName(_fromUtf8("comboAtributos"))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.tableWidget = QtGui.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 531, 101))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.etiquetaBuscar = QtGui.QLabel(self.tab_2)
        self.etiquetaBuscar.setGeometry(QtCore.QRect(0, 20, 101, 20))
        self.etiquetaBuscar.setObjectName(_fromUtf8("etiquetaBuscar"))
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 250, 531, 101))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.botonBuscar_2 = QtGui.QPushButton(self.tab_2)
        self.botonBuscar_2.setGeometry(QtCore.QRect(190, 220, 191, 27))
        self.botonBuscar_2.setObjectName(_fromUtf8("botonBuscar_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 160, 211, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.pushButton = QtGui.QPushButton(ventana)
        self.pushButton.setGeometry(QtCore.QRect(240, 520, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(ventana)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ventana)

    def retranslateUi(self, ventana):
        ventana.setWindowTitle(_translate("ventana", "Dialog", None))
        self.etiquetaTitulo_2.setText(_translate("ventana", "CIER-SUR", None))
        self.botonBuscar.setText(_translate("ventana", "Buscar", None))
        self.comboAtributos.setItemText(0, _translate("ventana", "Nombre Curso", None))
        self.comboAtributos.setItemText(1, _translate("ventana", "ID Curso", None))
        self.etiquetaBuscar.setText(_translate("ventana", "Consultar por:", None))
        self.botonBuscar_2.setText(_translate("ventana", "Consultar listado completo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ventana", "Consultar notas", None))
        self.tab.setToolTip(_translate("ventana", "<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton_2.setText(_translate("ventana", "Generar certificado de notas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ventana", "Generar reportes", None))
        self.pushButton.setText(_translate("ventana", "Cerrar", None))

class VentanaAgregarCohorte(QtGui.QFrame):
    def __init__(self):
        super(VentanaAgregarCohorte, self).__init__()
        self.setupUi(self)
    
    def asignarIDCurso(self, id_):
		self.id_curso = id_
    
    def agregarCohorte(self):
		global clienteSocket
		cohorte = str(self.campoCohorteID.text())
		if cohorte == '':
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("El campo cohorte no puede estar vacio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			return
		else:
			datos = {'funcion':'insertarCursoCohorte', 'parametros':{'id_course_fk':self.id_curso, 'cohort':cohorte}}
			clienteSocket.enviarMensaje(datos)
			res = clienteSocket.recibirRespuesta(False)
			if 'ok' in res:
				msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Bien"),_fromUtf8("La cohorte se ingreso correctamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			elif 'error' in res:
				msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("La cohorte no pudo ser ingresada"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

    def setupUi(self, VentanaAgregarCohorte):
        VentanaAgregarCohorte.setObjectName(_fromUtf8("VentanaAgregarCohorte"))
        VentanaAgregarCohorte.resize(421, 229)
        VentanaAgregarCohorte.setFrameShape(QtGui.QFrame.StyledPanel)
        VentanaAgregarCohorte.setFrameShadow(QtGui.QFrame.Raised)
        self.etiquetaTitulo = QtGui.QLabel(VentanaAgregarCohorte)
        self.etiquetaTitulo.setGeometry(QtCore.QRect(90, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitulo.setFont(font)
        self.etiquetaTitulo.setObjectName(_fromUtf8("etiquetaTitulo"))
        self.formLayoutWidget = QtGui.QWidget(VentanaAgregarCohorte)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 80, 291, 51))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.etiquetaCohorteID = QtGui.QLabel(self.formLayoutWidget)
        self.etiquetaCohorteID.setObjectName(_fromUtf8("etiquetaCohorteID"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.etiquetaCohorteID)
        self.campoCohorteID = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCohorteID.setObjectName(_fromUtf8("campoCohorteID"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.campoCohorteID)
        self.botonAgregar = QtGui.QPushButton(VentanaAgregarCohorte)
        self.botonAgregar.setGeometry(QtCore.QRect(130, 160, 141, 27))
        self.botonAgregar.setObjectName(_fromUtf8("botonAgregar"))

        self.retranslateUi(VentanaAgregarCohorte)
        QtCore.QObject.connect(self.botonAgregar, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregarCohorte)
        QtCore.QMetaObject.connectSlotsByName(VentanaAgregarCohorte)

    def retranslateUi(self, VentanaAgregarCohorte):
        VentanaAgregarCohorte.setWindowTitle(_translate("VentanaAgregarCohorte", "Frame", None))
        self.etiquetaTitulo.setText(_translate("VentanaAgregarCohorte", "Agregar Cohortes", None))
        self.etiquetaCohorteID.setText(_translate("VentanaAgregarCohorte", "Cohorte ID:", None))
        self.botonAgregar.setText(_translate("VentanaAgregarCohorte", "Agregar a curso", None))

class VentanaAgregarActividad(QtGui.QFrame):
    def __init__(self):
        super(VentanaAgregarActividad, self).__init__()
        self.setupUi(self)
        
    def asignarIDCurso(self, id_):
		self.id_curso = id_
	
    def agregarActividad(self):
		global clienteSocket
		actividad = str(self.campoIDActividad.text())
		inicio = self.selectorFechaInicio.date() #.toString("yyyy.MM.dd"))
		fin = self.selectorFechaFin.date() #.toString("yyyy.MM.dd"))
		if actividad == '':
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("El campo actividad no puede estar vacio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			return
		if (inicio.year() > fin.year()) or (inicio.year() < fin.year() and inicio.month() > fin.month()) or (inicio.year() < fin.year() and inicio.month() < fin.month() and inicio.day() > fin.day()):
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("Las fechas deben ser coherentes"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			return
		peso = str(self.campoPeso.text())
		datos = {'funcion': 'insertarCursoActividad', 
				'parametros':{'start_date': str(inicio.toString("yyyy.MM.dd")),
				               'end_date':str(fin.toString("yyyy.MM.dd")),
				               'id_course_fk': self.id_curso,
				               'activity': actividad,
				               'weight': peso
				               }}
		clienteSocket.enviarMensaje(datos)
		res = clienteSocket.recibirRespuesta(False)
		if 'ok' in res:
			msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("Actividad agregada correctamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
		elif 'error' in res:
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("La actividad no pudo ser agregada"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			

    def setupUi(self, VentanaAgregarActividad):
        VentanaAgregarActividad.setObjectName(_fromUtf8("VentanaAgregarActividad"))
        VentanaAgregarActividad.resize(435, 337)
        VentanaAgregarActividad.setFrameShape(QtGui.QFrame.StyledPanel)
        VentanaAgregarActividad.setFrameShadow(QtGui.QFrame.Raised)
        self.etiquetaTitulo = QtGui.QLabel(VentanaAgregarActividad)
        self.etiquetaTitulo.setGeometry(QtCore.QRect(110, 30, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitulo.setFont(font)
        self.etiquetaTitulo.setObjectName(_fromUtf8("etiquetaTitulo"))
        self.formLayoutWidget = QtGui.QWidget(VentanaAgregarActividad)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 90, 311, 111))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.etiquetaIDActividad = QtGui.QLabel(self.formLayoutWidget)
        self.etiquetaIDActividad.setObjectName(_fromUtf8("etiquetaIDActividad"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.etiquetaIDActividad)
        self.etiquetaFechaInicio = QtGui.QLabel(self.formLayoutWidget)
        self.etiquetaFechaInicio.setObjectName(_fromUtf8("etiquetaFechaInicio"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.etiquetaFechaInicio)
        self.etiquetaFechaFin = QtGui.QLabel(self.formLayoutWidget)
        self.etiquetaFechaFin.setObjectName(_fromUtf8("etiquetaFechaFin"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.etiquetaFechaFin)
        self.selectorFechaInicio = QtGui.QDateEdit(self.formLayoutWidget)
        self.selectorFechaInicio.setObjectName(_fromUtf8("selectorFechaInicio"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.selectorFechaInicio)
        self.campoIDActividad = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoIDActividad.setObjectName(_fromUtf8("campoIDActividad"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.campoIDActividad)
        self.selectorFechaFin = QtGui.QDateEdit(self.formLayoutWidget)
        self.selectorFechaFin.setObjectName(_fromUtf8("selectorFechaFin"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.selectorFechaFin)
        self.etiquetaPeso = QtGui.QLabel(self.formLayoutWidget)
        self.etiquetaPeso.setObjectName(_fromUtf8("etiquetaPeso"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.etiquetaPeso)
        self.campoPeso = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoPeso.setObjectName(_fromUtf8("campoPeso"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.campoPeso)
        self.botonAgregar = QtGui.QPushButton(VentanaAgregarActividad)
        self.botonAgregar.setGeometry(QtCore.QRect(150, 230, 131, 27))
        self.botonAgregar.setObjectName(_fromUtf8("botonAgregar"))

        self.retranslateUi(VentanaAgregarActividad)
        QtCore.QObject.connect(self.botonAgregar, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregarActividad)
        QtCore.QMetaObject.connectSlotsByName(VentanaAgregarActividad)
        
    def retranslateUi(self, VentanaAgregarActividad):
        VentanaAgregarActividad.setWindowTitle(_translate("VentanaAgregarActividad", "VentanaAgregarActividad", None))
        self.etiquetaTitulo.setText(_translate("VentanaAgregarActividad", "Agregar Actividades", None))
        self.etiquetaIDActividad.setText(_translate("VentanaAgregarActividad", "ID actividad", None))
        self.etiquetaFechaInicio.setText(_translate("VentanaAgregarActividad", "Fecha Inicio", None))
        self.etiquetaFechaFin.setText(_translate("VentanaAgregarActividad", "Fecha Fin", None))
        self.etiquetaPeso.setText(_translate("Frame", "Peso:", None))
        self.botonAgregar.setText(_translate("VentanaAgregarActividad", "Agregar a curso", None))

class VentanaAdministrarCursos(QtGui.QFrame):
	def mostrarVentanaAgregarActividad(self):
		self.ventanaAgregarAct.asignarIDCurso(str(self.campoCrearIdCurso.text()))
		self.ventanaAgregarAct.show()
		
	def mostrarVentanaAgregarCohorte(self):
		txt = str(self.campoCrearIdCurso.text())
		if txt == '':
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("El campo id del curso no puede estar vacio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			return
		self.ventanaAgregarCoh.asignarIDCurso(txt)
		self.ventanaAgregarCoh.show()

	def __init__(self):
		self.ventanaAgregarAct = VentanaAgregarActividad()
		self.ventanaAgregarCoh = VentanaAgregarCohorte()
		super(VentanaAdministrarCursos, self).__init__()
		self.setupUi(self)

	def setupUi(self, VentanaAdministrarCursos):
		VentanaAdministrarCursos.setObjectName(_fromUtf8("VentanaAdministrarCursos"))
		VentanaAdministrarCursos.resize(896, 325)
		self.tabWidget = QtGui.QTabWidget(VentanaAdministrarCursos)
		self.tabWidget.setGeometry(QtCore.QRect(0, 0, 891, 371))
		self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
		self.Buscar = QtGui.QWidget()
		self.Buscar.setObjectName(_fromUtf8("Buscar"))
		self.botonBuscarCurso = QtGui.QPushButton(self.Buscar)
		self.botonBuscarCurso.setGeometry(QtCore.QRect(30, 180, 98, 27))
		self.botonBuscarCurso.setObjectName(_fromUtf8("botonBuscarCurso"))
		self.campoBuscarIdCurso = QtGui.QLineEdit(self.Buscar)
		self.campoBuscarIdCurso.setGeometry(QtCore.QRect(110, 20, 113, 27))
		self.campoBuscarIdCurso.setObjectName(_fromUtf8("campoBuscarIdCurso"))
		self.etiquetaBuscarIdCurso = QtGui.QLabel(self.Buscar)
		self.etiquetaBuscarIdCurso.setGeometry(QtCore.QRect(20, 30, 66, 17))
		self.etiquetaBuscarIdCurso.setObjectName(_fromUtf8("etiquetaBuscarIdCurso"))
		#self.etiquetaBuscarDescripcionCurso = QtGui.QLabel(self.Buscar)
		#self.etiquetaBuscarDescripcionCurso.setGeometry(QtCore.QRect(20, 60, 91, 17))
		#self.etiquetaBuscarDescripcionCurso.setObjectName(_fromUtf8("etiquetaBuscarDescripcionCurso"))
		#self.etiquetaBuscarInicioCurso = QtGui.QLabel(self.Buscar)
		#self.etiquetaBuscarInicioCurso.setGeometry(QtCore.QRect(20, 90, 66, 17))
		#self.etiquetaBuscarInicioCurso.setObjectName(_fromUtf8("etiquetaBuscarInicioCurso"))
		#self.etiquetaBuscarFinCurso = QtGui.QLabel(self.Buscar)
		#self.etiquetaBuscarFinCurso.setGeometry(QtCore.QRect(20, 120, 66, 17))
		#self.etiquetaBuscarFinCurso.setObjectName(_fromUtf8("etiquetaBuscarFinCurso"))
		#self.campoBuscarDescripcionCurso = QtGui.QLineEdit(self.Buscar)
		#self.campoBuscarDescripcionCurso.setGeometry(QtCore.QRect(110, 50, 113, 27))
		#self.campoBuscarDescripcionCurso.setObjectName(_fromUtf8("campoBuscarDescripcionCurso"))
		#self.campoBuscarInicioCurso = QtGui.QLineEdit(self.Buscar)
		#self.campoBuscarInicioCurso.setGeometry(QtCore.QRect(110, 80, 113, 27))
		#self.campoBuscarInicioCurso.setObjectName(_fromUtf8("campoBuscarInicioCurso"))
		#self.campoBuscarFinCurso = QtGui.QLineEdit(self.Buscar)
		#self.campoBuscarFinCurso.setGeometry(QtCore.QRect(110, 110, 113, 27))
		#self.campoBuscarFinCurso.setObjectName(_fromUtf8("campoBuscarFinCurso"))
		self.etiquetaBuscarActividadesCurso = QtGui.QLabel(self.Buscar)
		self.etiquetaBuscarActividadesCurso.setGeometry(QtCore.QRect(250, 0, 161, 17))
		self.etiquetaBuscarActividadesCurso.setObjectName(_fromUtf8("etiquetaBuscarActividadesCurso"))
		self.listaBuscarCurso = QtGui.QListWidget(self.Buscar)
		self.listaBuscarCurso.setGeometry(QtCore.QRect(240, 20, 641, 192))
		self.listaBuscarCurso.setObjectName(_fromUtf8("listaBuscarCurso"))
		self.tabWidget.addTab(self.Buscar, _fromUtf8(""))
		self.tab_2 = QtGui.QWidget()
		self.tab_2.setObjectName(_fromUtf8("tab_2"))
		self.campoBorrarCurso = QtGui.QLineEdit(self.tab_2)
		self.campoBorrarCurso.setGeometry(QtCore.QRect(90, 40, 113, 27))
		self.campoBorrarCurso.setObjectName(_fromUtf8("campoBorrarCurso"))
		self.etiquetaBorrarCurso = QtGui.QLabel(self.tab_2)
		self.etiquetaBorrarCurso.setGeometry(QtCore.QRect(20, 50, 66, 17))
		self.etiquetaBorrarCurso.setObjectName(_fromUtf8("etiquetaBorrarCurso"))
		self.botonBorrarCurso = QtGui.QPushButton(self.tab_2)
		self.botonBorrarCurso.setGeometry(QtCore.QRect(240, 40, 98, 27))
		self.botonBorrarCurso.setObjectName(_fromUtf8("botonBorrarCurso"))
		self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
		self.tab_3 = QtGui.QWidget()
		self.tab_3.setObjectName(_fromUtf8("tab_3"))
		self.campoCrearIdCurso = QtGui.QLineEdit(self.tab_3)
		self.campoCrearIdCurso.setGeometry(QtCore.QRect(200, 40, 113, 27))
		self.campoCrearIdCurso.setObjectName(_fromUtf8("campoCrearIdCurso"))
		self.campoCrearDescripcionCurso = QtGui.QLineEdit(self.tab_3)
		self.campoCrearDescripcionCurso.setGeometry(QtCore.QRect(200, 70, 113, 27))
		self.campoCrearDescripcionCurso.setObjectName(_fromUtf8("campoCrearDescripcionCurso"))
		self.etiquetaCrearIdCurso = QtGui.QLabel(self.tab_3)
		self.etiquetaCrearIdCurso.setGeometry(QtCore.QRect(40, 40, 66, 17))
		self.etiquetaCrearIdCurso.setObjectName(_fromUtf8("etiquetaCrearIdCurso"))
		self.etiquetaCrearDescripcionCurso = QtGui.QLabel(self.tab_3)
		self.etiquetaCrearDescripcionCurso.setGeometry(QtCore.QRect(40, 70, 91, 17))
		self.etiquetaCrearDescripcionCurso.setObjectName(_fromUtf8("etiquetaCrearDescripcionCurso"))
		self.etiquetaCrearInicioCurso = QtGui.QLabel(self.tab_3)
		self.etiquetaCrearInicioCurso.setGeometry(QtCore.QRect(40, 110, 66, 17))
		self.etiquetaCrearInicioCurso.setObjectName(_fromUtf8("etiquetaCrearInicioCurso"))
		self.etiquetaCrearFinCurso = QtGui.QLabel(self.tab_3)
		self.etiquetaCrearFinCurso.setGeometry(QtCore.QRect(40, 140, 66, 17))
		self.etiquetaCrearFinCurso.setObjectName(_fromUtf8("etiquetaCrearFinCurso"))
		self.campoCrearInicioCurso = QtGui.QDateEdit(self.tab_3)
		self.campoCrearInicioCurso.setGeometry(QtCore.QRect(200, 100, 110, 27))
		self.campoCrearInicioCurso.setObjectName(_fromUtf8("campoCrearInicioCurso"))
		self.campoCrearFinCurso = QtGui.QDateEdit(self.tab_3)
		self.campoCrearFinCurso.setGeometry(QtCore.QRect(200, 130, 110, 27))
		self.campoCrearFinCurso.setObjectName(_fromUtf8("campoCrearFinCurso"))
		self.botonCrearAgregarActividadCurso = QtGui.QPushButton(self.tab_3)
		self.botonCrearAgregarActividadCurso.setGeometry(QtCore.QRect(370, 40, 131, 27))
		self.botonCrearAgregarActividadCurso.setObjectName(_fromUtf8("botonCrearAgregarActividadCurso"))
		self.botonCrearCurso = QtGui.QPushButton(self.tab_3)
		self.botonCrearCurso.setGeometry(QtCore.QRect(370, 140, 98, 27))
		self.botonCrearCurso.setObjectName(_fromUtf8("botonCrearCurso"))
		self.botonCrearAgregarCohorteCurso = QtGui.QPushButton(self.tab_3)
		self.botonCrearAgregarCohorteCurso.setGeometry(QtCore.QRect(370, 90, 131, 27))
		self.botonCrearAgregarCohorteCurso.setObjectName(_fromUtf8("botonCrearAgregarCohorteCurso"))
		self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
		self.tab = QtGui.QWidget()
		self.tab.setObjectName(_fromUtf8("tab"))
		self.campoEditarIdcurso = QtGui.QLineEdit(self.tab)
		self.campoEditarIdcurso.setGeometry(QtCore.QRect(170, 40, 113, 27))
		self.campoEditarIdcurso.setObjectName(_fromUtf8("campoEditarIdcurso"))
		self.campoEditardescripcioncurso = QtGui.QLineEdit(self.tab)
		self.campoEditardescripcioncurso.setGeometry(QtCore.QRect(170, 70, 113, 27))
		self.campoEditardescripcioncurso.setObjectName(_fromUtf8("campoEditardescripcioncurso"))
		self.campoEditarFincurso = QtGui.QDateEdit(self.tab)
		self.campoEditarFincurso.setGeometry(QtCore.QRect(170, 130, 110, 27))
		self.campoEditarFincurso.setObjectName(_fromUtf8("campoEditarFincurso"))
		self.campoEditarIniciocurso = QtGui.QDateEdit(self.tab)
		self.campoEditarIniciocurso.setGeometry(QtCore.QRect(170, 100, 110, 27))
		self.campoEditarIniciocurso.setObjectName(_fromUtf8("campoEditarIniciocurso"))
		self.label_7 = QtGui.QLabel(self.tab)
		self.label_7.setGeometry(QtCore.QRect(30, 50, 66, 17))
		self.label_7.setObjectName(_fromUtf8("label_7"))
		self.label_8 = QtGui.QLabel(self.tab)
		self.label_8.setGeometry(QtCore.QRect(30, 80, 91, 17))
		self.label_8.setObjectName(_fromUtf8("label_8"))
		self.label_9 = QtGui.QLabel(self.tab)
		self.label_9.setGeometry(QtCore.QRect(30, 110, 66, 17))
		self.label_9.setObjectName(_fromUtf8("label_9"))
		self.label_10 = QtGui.QLabel(self.tab)
		self.label_10.setGeometry(QtCore.QRect(30, 140, 66, 17))
		self.label_10.setObjectName(_fromUtf8("label_10"))
		self.botonEditarActividadCurso = QtGui.QPushButton(self.tab)
		self.botonEditarActividadCurso.setGeometry(QtCore.QRect(380, 70, 121, 27))
		self.botonEditarActividadCurso.setObjectName(_fromUtf8("botonEditarActividadCurso"))
		self.botonEditarCurso = QtGui.QPushButton(self.tab)
		self.botonEditarCurso.setGeometry(QtCore.QRect(380, 20, 121, 27))
		self.botonEditarCurso.setObjectName(_fromUtf8("botonEditarCurso"))
		self.botonEditarCohorteCurso = QtGui.QPushButton(self.tab)
		self.botonEditarCohorteCurso.setGeometry(QtCore.QRect(380, 120, 131, 27))
		self.botonEditarCohorteCurso.setObjectName(_fromUtf8("botonEditarCohorteCurso"))
		self.tabWidget.addTab(self.tab, _fromUtf8(""))
		self.retranslateUi(VentanaAdministrarCursos)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QObject.connect(self.botonBuscarCurso, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaAdministrarCursos.buscarCurso)
		QtCore.QObject.connect(self.botonCrearAgregarActividadCurso, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaAdministrarCursos.mostrarVentanaAgregarActividad)
		QtCore.QObject.connect(self.botonCrearCurso, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaAdministrarCursos.agregarCurso)
		QtCore.QObject.connect(self.botonCrearAgregarCohorteCurso, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaAdministrarCursos.mostrarVentanaAgregarCohorte)
		QtCore.QMetaObject.connectSlotsByName(VentanaAdministrarCursos)

	def buscarCurso(self):
		global clienteSocket
		id_curso = str(self.campoBuscarIdCurso.text())
		self.listaBuscarCurso.clear()
		if id_curso != '':
			datos = {'funcion':'consultarCursoPorID', 'parametros': {'id':id_curso}}
			clienteSocket.enviarMensaje(datos)
			ls = clienteSocket.recibirRespuesta(True)
			for item in ls:
				str_item = "|"
				for cad in item:
					str_item += cad + "|"
				self.listaBuscarCurso.addItem(QtGui.QListWidgetItem(_fromUtf8(str_item), self.listaBuscarCurso, 0))
		else:
			datos = {'funcion': 'consultarCursos', 'parametros':{}}
			clienteSocket.enviarMensaje(datos)
			ls = clienteSocket.recibirRespuesta(True)
			for item in ls:
				str_item = "|"
				for cad in item:
					str_item += cad + "|"
				self.listaBuscarCurso.addItem(QtGui.QListWidgetItem(_fromUtf8(str_item), self.listaBuscarCurso, 0))

	def agregarCurso(self):
		global clienteSocket
		id_ = str(self.campoCrearIdCurso.text())
		descripcion = str(self.campoCrearDescripcionCurso.text())
		inicio = self.campoCrearInicioCurso.date().toString("yyyy.MM.dd")
		fin = self.campoCrearFinCurso.date().toString("yyyy.MM.dd")
		datos = {'funcion':'insertarCurso', 'parametros':{'id':id_, 'end_date':str(fin), 
						'start_date':str(inicio), 'description':descripcion}
		}
		clienteSocket.enviarMensaje(datos)
		res = clienteSocket.recibirRespuesta(False)
		if 'ok' in res:
			msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("El curso se agrego correctamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
		elif 'error' in res:
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("El curso no se agrego correctamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)



	def retranslateUi(self, VentanaAdministrarCursos):
		VentanaAdministrarCursos.setWindowTitle(_translate("VentanaAdministrarCursos", "Form", None))
		self.botonBuscarCurso.setText(_translate("VentanaAdministrarCursos", "Buscar", None))
		self.etiquetaBuscarIdCurso.setText(_translate("VentanaAdministrarCursos", "ID", None))
		#self.etiquetaBuscarDescripcionCurso.setText(_translate("VentanaAdministrarCursos", "Descripcion", None))
		#self.etiquetaBuscarInicioCurso.setText(_translate("VentanaAdministrarCursos", "Inicio", None))
		#self.etiquetaBuscarFinCurso.setText(_translate("VentanaAdministrarCursos", "Fin", None))
		#self.etiquetaBuscarActividadesCurso.setText(_translate("VentanaAdministrarCursos", "Resultados", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.Buscar), _translate("VentanaAdministrarCursos", "Buscar", None))
		self.etiquetaBorrarCurso.setText(_translate("VentanaAdministrarCursos", "ID", None))
		self.botonBorrarCurso.setText(_translate("VentanaAdministrarCursos", "Borrar", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("VentanaAdministrarCursos", "Borrar", None))
		self.etiquetaCrearIdCurso.setText(_translate("VentanaAdministrarCursos", "ID", None))
		self.etiquetaCrearDescripcionCurso.setText(_translate("VentanaAdministrarCursos", "Descripcion", None))
		self.etiquetaCrearInicioCurso.setText(_translate("VentanaAdministrarCursos", "Inicio", None))
		self.etiquetaCrearFinCurso.setText(_translate("VentanaAdministrarCursos", "Fin", None))
		self.botonCrearAgregarActividadCurso.setText(_translate("VentanaAdministrarCursos", "Agregar Actividad", None))
		self.botonCrearCurso.setText(_translate("VentanaAdministrarCursos", "Crear Curso", None))
		self.botonCrearAgregarCohorteCurso.setText(_translate("VentanaAdministrarCursos", "Agregar Cohorte", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("VentanaAdministrarCursos", "Crear", None))
		self.label_7.setText(_translate("VentanaAdministrarCursos", "ID", None))
		self.label_8.setText(_translate("VentanaAdministrarCursos", "Descripcion", None))
		self.label_9.setText(_translate("VentanaAdministrarCursos", "Inicio", None))
		self.label_10.setText(_translate("VentanaAdministrarCursos", "Fin", None))
		self.botonEditarActividadCurso.setText(_translate("VentanaAdministrarCursos", "Editar Actividad", None))
		self.botonEditarCurso.setText(_translate("VentanaAdministrarCursos", "Editar Curso", None))
		self.botonEditarCohorteCurso.setText(_translate("VentanaAdministrarCursos", "Editar Cohorte", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("VentanaAdministrarCursos", "Editar", None))

class VentanaOpcionesAdm(QtGui.QFrame):
    def __init__(self):
        super(VentanaOpcionesAdm, self).__init__()
        self.ventanaAdmCursos = VentanaAdministrarCursos()
        self.ventanaOpRegAdm = VentanaOpcionesRegistroAdm()
        self.setupUi(self)
        
    def mostrarAdmCursos(self):
		self.ventanaAdmCursos.show()

    def ingresarListaBecados(self):
		global clienteSocket
		ruta = QtGui.QFileDialog.getOpenFileName(None, _fromUtf8("Open File"), "/home", _fromUtf8("Files (*.txt *.ini)"))
		archivo = open(ruta, 'r')
		lineas = archivo.readlines()
		archivo.close()
		for i in range(0, len(lineas)):
			lineas[i] = lineas[i].replace("\n", "")
		datos = {'funcion':'activarLT', 'parametros': {'ids':lineas}}
		clienteSocket.enviarMensaje(datos)
		res = clienteSocket.recibirRespuesta(False);
		if 'ok' in res:
			msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("La lista de becados se ingreso correctamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
		elif 'error' in res:
			msgBox = QtGui.QMessageBox.warning(self, _fromUtf8("Error "),_fromUtf8("La lista de becados no se ingreso correctamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)


    def mostrarVentanaOpRegAdm(self):
        self.ventanaOpRegAdm.show()

    def setupUi(self, VentanaOpcionesAdm):
        VentanaOpcionesAdm.setObjectName(_fromUtf8("VentanaOpcionesAdm"))
        VentanaOpcionesAdm.resize(541, 322)
        VentanaOpcionesAdm.setFrameShape(QtGui.QFrame.StyledPanel)
        VentanaOpcionesAdm.setFrameShadow(QtGui.QFrame.Raised)
        self.etiquetaTitutlo = QtGui.QLabel(VentanaOpcionesAdm)
        self.etiquetaTitutlo.setGeometry(QtCore.QRect(170, 20, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitutlo.setFont(font)
        self.etiquetaTitutlo.setObjectName(_fromUtf8("etiquetaTitutlo"))
        self.botonEditarPerfil = QtGui.QPushButton(VentanaOpcionesAdm)
        self.botonEditarPerfil.setGeometry(QtCore.QRect(60, 90, 141, 27))
        self.botonEditarPerfil.setObjectName(_fromUtf8("botonEditarPerfil"))
        self.botonCerrarSesion = QtGui.QPushButton(VentanaOpcionesAdm)
        self.botonCerrarSesion.setGeometry(QtCore.QRect(410, 20, 98, 27))
        self.botonCerrarSesion.setObjectName(_fromUtf8("botonCerrarSesion"))
        self.botonAdmUsuarios = QtGui.QPushButton(VentanaOpcionesAdm)
        self.botonAdmUsuarios.setGeometry(QtCore.QRect(270, 90, 151, 27))
        self.botonAdmUsuarios.setObjectName(_fromUtf8("botonAdmUsuarios"))
        self.botonReportes = QtGui.QPushButton(VentanaOpcionesAdm)
        self.botonReportes.setGeometry(QtCore.QRect(60, 190, 121, 27))
        self.botonReportes.setObjectName(_fromUtf8("botonReportes"))
        self.botonAdmCursos = QtGui.QPushButton(VentanaOpcionesAdm)
        self.botonAdmCursos.setGeometry(QtCore.QRect(280, 190, 141, 27))
        self.botonAdmCursos.setObjectName(_fromUtf8("botonAdmCursos"))
        self.botonListaBecados = QtGui.QPushButton(VentanaOpcionesAdm)
        self.botonListaBecados.setGeometry(QtCore.QRect(60, 250, 161, 27))
        self.botonListaBecados.setObjectName(_fromUtf8("botonListaBecados"))

        self.retranslateUi(VentanaOpcionesAdm)
        #QtCore.QObject.connect(self.botonCancelar, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaOpcionesAdm.close)
        QtCore.QObject.connect(self.botonAdmCursos, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaOpcionesAdm.mostrarAdmCursos)
        QtCore.QObject.connect(self.botonListaBecados, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaOpcionesAdm.ingresarListaBecados)
        QtCore.QObject.connect(self.botonAdmUsuarios, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaOpcionesAdm.mostrarVentanaOpRegAdm)
        QtCore.QMetaObject.connectSlotsByName(VentanaOpcionesAdm)


    def retranslateUi(self, VentanaOpcionesAdm):
        VentanaOpcionesAdm.setWindowTitle(_translate("VentanaOpcionesAdm", "Opciones Adm", None))
        self.etiquetaTitutlo.setText(_translate("VentanaOpcionesAdm", "¿Qué Desea Hacer?", None))
        self.botonEditarPerfil.setText(_translate("VentanaOpcionesAdm", "Editar Perfil", None))
        self.botonCerrarSesion.setText(_translate("VentanaOpcionesAdm", "Cerrar sesión", None))
        self.botonAdmUsuarios.setText(_translate("VentanaOpcionesAdm", "Administrar Usuarios", None))
        self.botonReportes.setText(_translate("VentanaOpcionesAdm", "Ver Reportes", None))
        self.botonAdmCursos.setText(_translate("VentanaOpcionesAdm", "Administrar Cursos", None))
        self.botonListaBecados.setText(_translate("ventantaOpcionesAdm", "Ingresar Lista Becados", None))


class VentanaRegistroMT(QtGui.QFrame):
    def __init__(self):
        super(VentanaRegistroMT, self).__init__()
        self.setupUi(self)


    def setupUi(self, VentanaRegistroMT):
        VentanaRegistroMT.setObjectName(_fromUtf8("VentanaRegistroMT"))
        VentanaRegistroMT.resize(727, 611)
        VentanaRegistroMT.setStyleSheet(_fromUtf8(""))
        VentanaRegistroMT.setFrameShape(QtGui.QFrame.StyledPanel)
        VentanaRegistroMT.setFrameShadow(QtGui.QFrame.Raised)
        self.tabWidget = QtGui.QTabWidget(VentanaRegistroMT)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 721, 481))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.etiquetaNombres = QtGui.QLabel(self.tab)
        self.etiquetaNombres.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.etiquetaNombres.setObjectName(_fromUtf8("etiquetaNombres"))
        self.etiquetaApellidos = QtGui.QLabel(self.tab)
        self.etiquetaApellidos.setGeometry(QtCore.QRect(390, 30, 81, 16))
        self.etiquetaApellidos.setObjectName(_fromUtf8("etiquetaApellidos"))
        self.etiquetaID = QtGui.QLabel(self.tab)
        self.etiquetaID.setGeometry(QtCore.QRect(20, 110, 141, 16))
        self.etiquetaID.setObjectName(_fromUtf8("etiquetaID"))
        self.etiquetaCorreo = QtGui.QLabel(self.tab)
        self.etiquetaCorreo.setGeometry(QtCore.QRect(390, 110, 61, 16))
        self.etiquetaCorreo.setObjectName(_fromUtf8("etiquetaCorreo"))
        self.etiquetaTel = QtGui.QLabel(self.tab)
        self.etiquetaTel.setGeometry(QtCore.QRect(20, 190, 71, 16))
        self.etiquetaTel.setObjectName(_fromUtf8("etiquetaTel"))
        self.etiquetaDir = QtGui.QLabel(self.tab)
        self.etiquetaDir.setGeometry(QtCore.QRect(390, 190, 81, 16))
        self.etiquetaDir.setObjectName(_fromUtf8("etiquetaDir"))
        self.campoNombre = QtGui.QLineEdit(self.tab)
        self.campoNombre.setGeometry(QtCore.QRect(20, 60, 311, 23))
        self.campoNombre.setObjectName(_fromUtf8("campoNombre"))
        self.campoApellidos = QtGui.QLineEdit(self.tab)
        self.campoApellidos.setGeometry(QtCore.QRect(390, 60, 301, 23))
        self.campoApellidos.setObjectName(_fromUtf8("campoApellidos"))
        self.campoID = QtGui.QLineEdit(self.tab)
        self.campoID.setGeometry(QtCore.QRect(20, 140, 311, 23))
        self.campoID.setObjectName(_fromUtf8("campoID"))
        self.campoCorreo = QtGui.QLineEdit(self.tab)
        self.campoCorreo.setGeometry(QtCore.QRect(390, 140, 311, 23))
        self.campoCorreo.setText(_fromUtf8(""))
        self.campoCorreo.setObjectName(_fromUtf8("campoCorreo"))
        self.campoTel = QtGui.QLineEdit(self.tab)
        self.campoTel.setGeometry(QtCore.QRect(20, 220, 311, 23))
        self.campoTel.setObjectName(_fromUtf8("campoTel"))
        self.campoDir = QtGui.QLineEdit(self.tab)
        self.campoDir.setGeometry(QtCore.QRect(380, 220, 311, 23))
        self.campoDir.setObjectName(_fromUtf8("campoDir"))
        self.etiquetaSexo = QtGui.QLabel(self.tab)
        self.etiquetaSexo.setGeometry(QtCore.QRect(20, 270, 71, 16))
        self.etiquetaSexo.setObjectName(_fromUtf8("etiquetaSexo"))
        self.etiquetaFecha = QtGui.QLabel(self.tab)
        self.etiquetaFecha.setGeometry(QtCore.QRect(380, 270, 131, 16))
        self.etiquetaFecha.setObjectName(_fromUtf8("etiquetaFecha"))
        self.dateEdit = QtGui.QDateEdit(self.tab)
        self.dateEdit.setGeometry(QtCore.QRect(380, 300, 110, 29))
        self.dateEdit.setDate(QtCore.QDate(2015, 1, 1))
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(7999, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEdit.setMinimumDate(QtCore.QDate(1920, 1, 1))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.etiquetaEstadoCivil = QtGui.QLabel(self.tab)
        self.etiquetaEstadoCivil.setGeometry(QtCore.QRect(20, 350, 101, 16))
        self.etiquetaEstadoCivil.setObjectName(_fromUtf8("etiquetaEstadoCivil"))
        self.comboEstadosCiviles = QtGui.QComboBox(self.tab)
        self.comboEstadosCiviles.setGeometry(QtCore.QRect(20, 380, 101, 25))
        self.comboEstadosCiviles.setModelColumn(0)
        self.comboEstadosCiviles.setObjectName(_fromUtf8("comboEstadosCiviles"))
        self.comboEstadosCiviles.addItem(_fromUtf8(""))
        self.comboEstadosCiviles.addItem(_fromUtf8(""))
        self.comboEstadosCiviles.addItem(_fromUtf8(""))
        self.comboEstadosCiviles.addItem(_fromUtf8(""))
        self.comboSexo = QtGui.QComboBox(self.tab)
        self.comboSexo.setGeometry(QtCore.QRect(20, 300, 311, 23))
        self.comboSexo.setObjectName(_fromUtf8("comboSexo"))
        self.comboSexo.setModelColumn(0)
        self.comboSexo.addItem(_fromUtf8(""))
        self.comboSexo.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.etiquetaSede = QtGui.QLabel(self.tab_2)
        self.etiquetaSede.setGeometry(QtCore.QRect(330, 30, 171, 16))
        self.etiquetaSede.setObjectName(_fromUtf8("etiquetaSede"))
        self.etiquetaInstitucion = QtGui.QLabel(self.tab_2)
        self.etiquetaInstitucion.setGeometry(QtCore.QRect(20, 30, 211, 16))
        self.etiquetaInstitucion.setObjectName(_fromUtf8("etiquetaInstitucion"))
        self.etiquetaGrado = QtGui.QLabel(self.tab_2)
        self.etiquetaGrado.setGeometry(QtCore.QRect(20, 80, 54, 15))
        self.etiquetaGrado.setObjectName(_fromUtf8("etiquetaGrado"))
        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(20, 140, 54, 15))
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.etiquetaSecEd = QtGui.QLabel(self.tab_2)
        self.etiquetaSecEd.setGeometry(QtCore.QRect(320, 130, 251, 16))
        self.etiquetaSecEd.setObjectName(_fromUtf8("etiquetaSecEd"))
        self.etiquetaMunicipio = QtGui.QLabel(self.tab_2)
        self.etiquetaMunicipio.setGeometry(QtCore.QRect(320, 80, 91, 16))
        self.etiquetaMunicipio.setObjectName(_fromUtf8("etiquetaMunicipio"))
        self.etiquetaArea = QtGui.QLabel(self.tab_2)
        self.etiquetaArea.setGeometry(QtCore.QRect(20, 140, 211, 16))
        self.etiquetaArea.setObjectName(_fromUtf8("etiquetaArea"))
        self.etiquetaOtro = QtGui.QLabel(self.tab_2)
        self.etiquetaOtro.setGeometry(QtCore.QRect(20, 250, 31, 16))
        self.etiquetaOtro.setObjectName(_fromUtf8("etiquetaOtro"))
        self.campoOtro = QtGui.QLineEdit(self.tab_2)
        self.campoOtro.setGeometry(QtCore.QRect(60, 250, 161, 23))
        self.campoOtro.setObjectName(_fromUtf8("campoOtro"))
        self.campoSede = QtGui.QLineEdit(self.tab_2)
        self.campoSede.setGeometry(QtCore.QRect(20, 50, 261, 23))
        self.campoSede.setObjectName(_fromUtf8("campoSede"))
        self.campoInstitucion = QtGui.QLineEdit(self.tab_2)
        self.campoInstitucion.setGeometry(QtCore.QRect(320, 50, 291, 23))
        self.campoInstitucion.setObjectName(_fromUtf8("campoInstitucion"))
        self.campoGrado = QtGui.QLineEdit(self.tab_2)
        self.campoGrado.setGeometry(QtCore.QRect(20, 100, 261, 23))
        self.campoGrado.setObjectName(_fromUtf8("campoGrado"))
        self.campoSecEdu = QtGui.QLineEdit(self.tab_2)
        self.campoSecEdu.setGeometry(QtCore.QRect(320, 150, 281, 23))
        self.campoSecEdu.setObjectName(_fromUtf8("campoSecEdu"))
        self.campoMunicipio = QtGui.QLineEdit(self.tab_2)
        self.campoMunicipio.setGeometry(QtCore.QRect(320, 100, 291, 23))
        self.campoMunicipio.setObjectName(_fromUtf8("campoMunicipio"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 160, 271, 80))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radbtnMatematicas = QtGui.QRadioButton(self.groupBox)
        self.radbtnMatematicas.setGeometry(QtCore.QRect(0, 10, 151, 21))
        self.radbtnMatematicas.setObjectName(_fromUtf8("radbtnMatematicas"))
        self.radbtnCiencias = QtGui.QRadioButton(self.groupBox)
        self.radbtnCiencias.setGeometry(QtCore.QRect(0, 30, 261, 21))
        self.radbtnCiencias.setObjectName(_fromUtf8("radbtnCiencias"))
        self.radbtnLenguaje = QtGui.QRadioButton(self.groupBox)
        self.radbtnLenguaje.setGeometry(QtCore.QRect(0, 50, 95, 21))
        self.radbtnLenguaje.setObjectName(_fromUtf8("radbtnLenguaje"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(30, 350, 141, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.scrollArea_2 = QtGui.QScrollArea(self.tab_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(180, 300, 471, 111))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 469, 109))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.textEdit = QtGui.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(180, 300, 471, 111))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.etiquetaDep = QtGui.QLabel(self.tab_2)
        self.etiquetaDep.setGeometry(QtCore.QRect(320, 180, 251, 16))
        self.etiquetaDep.setObjectName(_fromUtf8("etiquetaDep"))
        self.comboDep = QtGui.QComboBox(self.tab_2)
        self.comboDep.setGeometry(QtCore.QRect(320, 200, 121, 25))
        self.comboDep.setObjectName(_fromUtf8("comboDep"))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.etiquetaExp = QtGui.QLabel(self.tab_3)
        self.etiquetaExp.setGeometry(QtCore.QRect(10, 80, 151, 17))
        self.etiquetaExp.setObjectName(_fromUtf8("etiquetaExp"))
        self.scrollArea = QtGui.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(210, 40, 461, 141))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 139))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.areaExp = QtGui.QTextEdit(self.tab_3)
        self.areaExp.setGeometry(QtCore.QRect(210, 40, 461, 141))
        self.areaExp.setObjectName(_fromUtf8("areaExp"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.etiquetaTitulo = QtGui.QLabel(VentanaRegistroMT)
        self.etiquetaTitulo.setGeometry(QtCore.QRect(300, 0, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitulo.setFont(font)
        self.etiquetaTitulo.setObjectName(_fromUtf8("etiquetaTitulo"))
        self.etiquetaSubTit1 = QtGui.QLabel(VentanaRegistroMT)
        self.etiquetaSubTit1.setGeometry(QtCore.QRect(70, 20, 581, 20))
        self.etiquetaSubTit1.setObjectName(_fromUtf8("etiquetaSubTit1"))
        self.etiquetaSubTit2 = QtGui.QLabel(VentanaRegistroMT)
        self.etiquetaSubTit2.setGeometry(QtCore.QRect(310, 40, 101, 16))
        self.etiquetaSubTit2.setStyleSheet(_fromUtf8("color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));"))
        self.etiquetaSubTit2.setObjectName(_fromUtf8("etiquetaSubTit2"))
        self.botonEnviar = QtGui.QPushButton(VentanaRegistroMT)
        self.botonEnviar.setGeometry(QtCore.QRect(170, 570, 91, 24))
        self.botonEnviar.setObjectName(_fromUtf8("botonEnviar"))
        self.botonSalir = QtGui.QPushButton(VentanaRegistroMT)
        self.botonSalir.setGeometry(QtCore.QRect(410, 570, 91, 24))
        self.botonSalir.setObjectName(_fromUtf8("botonSalir"))

        #print "en setupUi", type(self.comboSexo)
        self.retranslateUi(VentanaRegistroMT)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VentanaRegistroMT)
        QtCore.QObject.connect(self.botonSalir, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaRegistroMT.close)
        QtCore.QObject.connect(self.botonEnviar, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaRegistroMT.registrarMT)

    def retranslateUi(self, VentanaRegistroMT):
        VentanaRegistroMT.setWindowTitle(_translate("VentanaRegistroMT", "Frame", None))
        self.etiquetaNombres.setText(_translate("VentanaRegistroMT", "Nombres *", None))
        self.etiquetaApellidos.setText(_translate("VentanaRegistroMT", "Apellidos *", None))
        self.etiquetaID.setText(_translate("VentanaRegistroMT", "Num. Identificación *", None))
        self.etiquetaCorreo.setText(_translate("VentanaRegistroMT", "Correo *", None))
        self.etiquetaTel.setText(_translate("VentanaRegistroMT", "Teléfono *", None))
        self.etiquetaDir.setText(_translate("VentanaRegistroMT", "Dirección *", None))
        self.etiquetaSexo.setText(_translate("VentanaRegistroMT", "Sexo *", None))
        self.etiquetaFecha.setText(_translate("VentanaRegistroMT", "Fecha Nacimiento *", None))
        self.etiquetaEstadoCivil.setText(_translate("VentanaRegistroMT", "Estado civil *", None))
        self.comboEstadosCiviles.setItemText(0, _translate("VentanaRegistroMT", "Soltero", None))
        self.comboEstadosCiviles.setItemText(1, _translate("VentanaRegistroMT", "Casado", None))
        self.comboEstadosCiviles.setItemText(2, _translate("VentanaRegistroMT", "Viudo", None))
        self.comboEstadosCiviles.setItemText(3, _translate("VentanaRegistroMT", "Union Libre", None))
        self.comboSexo.setItemText(0, _translate("VentanaRegistroMT", "Masculino", None))
        self.comboSexo.setItemText(1, _translate("VentanaRegistroMT", "Femenino", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("VentanaRegistroMT", "Información Personal", None))
        self.etiquetaSede.setText(_translate("VentanaRegistroMT", "Sede a la que pertenece *", None))
        self.etiquetaInstitucion.setText(_translate("VentanaRegistroMT", "Institución a la que pertenece *", None))
        self.etiquetaGrado.setText(_translate("VentanaRegistroMT", "Grado *", None))
        self.etiquetaSecEd.setText(_translate("VentanaRegistroMT", "Secretaría de Educación *", None))
        self.etiquetaMunicipio.setText(_translate("VentanaRegistroMT", "Municipio *", None))
        self.etiquetaArea.setText(_translate("VentanaRegistroMT", "Área a la cual se va a inscribir *", None))
        self.etiquetaOtro.setText(_translate("VentanaRegistroMT", "Otro:", None))
        self.radbtnMatematicas.setText(_translate("VentanaRegistroMT", " Matemáticas", None))
        self.radbtnCiencias.setText(_translate("VentanaRegistroMT", "Ciencias Naturales y Ed. Ambiental    ", None))
        self.radbtnLenguaje.setText(_translate("VentanaRegistroMT", "Lenguaje", None))
        self.label.setText(_translate("VentanaRegistroMT", "Historial Académico", None))
        self.etiquetaDep.setText(_translate("VentanaRegistroMT", "Departamento *", None))
        self.comboDep.setItemText(0, _translate("VentanaRegistroMT", "Valle del Cauca", None))
        self.comboDep.setItemText(1, _translate("VentanaRegistroMT", "Nariño", None))
        self.comboDep.setItemText(2, _translate("VentanaRegistroMT", "Tolima", None))
        self.comboDep.setItemText(3, _translate("VentanaRegistroMT", "Cauca", None))
        self.comboDep.setItemText(4, _translate("VentanaRegistroMT", "Huila", None))
        self.comboDep.setItemText(5, _translate("VentanaRegistroMT", "Caqueta", None))
        self.comboDep.setItemText(6, _translate("VentanaRegistroMT", "Putumayo", None))
        self.comboDep.setItemText(7, _translate("VentanaRegistroMT", "Amazonas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("VentanaRegistroMT", "Información Profesional", None))
        self.etiquetaExp.setText(_translate("VentanaRegistroMT", "Experiencia Laboral:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("VentanaRegistroMT", "Adicional", None))
        self.etiquetaTitulo.setText(_translate("VentanaRegistroMT", "CIER-SUR", None))
        self.etiquetaSubTit1.setText(_translate("VentanaRegistroMT", "Formulario de inscripción de profesores al programa de formación CREA-TIC / CIER-SUR", None))
        self.etiquetaSubTit2.setText(_translate("VentanaRegistroMT", "(*) Obligatorio", None))
        self.botonEnviar.setText(_translate("VentanaRegistroMT", "Enviar", None))
        self.botonSalir.setText(_translate("VentanaRegistroMT", "Salir", None))
        #print "en retranslateUi ", type(self.comboSexo)

    def recuperarDatos(self):
        index = self.comboSexo.currentIndex()
        sex = ''
        if index == 0:
            sex = 'M'
        else:
            sex = 'F'
        #sexo = self.comboSexo().currentText()
        nombres = str(self.campoNombre.text())
        if nombres == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo Nombres es obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        apellidos = str(self.campoApellidos.text())
        if apellidos == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo Apellidos es obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        id_ = str(self.campoID.text())
        if id_ == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo Identificación es obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        correo = str(self.campoCorreo.text())
        if correo == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo correo es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        tel = str(self.campoTel.text())
        if tel == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo telefono es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        direccion = str(self.campoDir.text())
        if direccion == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo direccion es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        fechaNacimiento = str(self.dateEdit.date().toString("yyyy.MM.dd"))
        print fechaNacimiento
        estadoCivil = str(self.comboEstadosCiviles.currentText())
        institucion = str(self.campoInstitucion.text())
        if institucion == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo institución es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        grado = str(self.campoGrado.text())
        if grado == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo grado es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        sede = str(self.campoSede.text())
        municipio = str(self.campoMunicipio.text())
        if municipio == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo municipio es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        secretaria = str(self.campoSecEdu.text())
        if secretaria == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo Secretaría es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        departamento = str(self.comboDep.currentText())
        area = ''
        if self.radbtnMatematicas.isChecked():
            area = 'Matemáticas'
        elif self.radbtnLenguaje.isChecked():
            area = 'Lenguaje'
        elif self.radbtnCiencias.isChecked():
            area = 'Ciencias'
        else:
            area = str(self.campoOtro.text())
        historialAcademico = ''
        experienciaLaboral = ''
        try:
            txt1 = str(self.textEdit.toPlainText())
            historialAcademico = txt1.split("\n")
            #historialAcademico = txt1.split(",")
            txt2 = str(self.areaExp.toPlainText())
            #text2 = txt2.replace("\n", "")
            experienciaLaboral = txt2.split("\n")
        except Exception as ex:
            print ex
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("La experiencia laboral y \n el historial academico deben tener todos sus items separados por comas"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

        pass_ = nombres[0] + id_ + apellidos[0]

        dictDatos = {'first_name':nombres, 'last_name':apellidos, 'id': id_, 'email': correo, 'tel_num':tel, 'is_active': False,
                    'address': direccion, 'sex': sex, 'birth_date': fechaNacimiento, 'marital_status': estadoCivil,
                    'institution': institucion, 'grade': grado, 'city':municipio, 'area':area, 'secretariat':secretaria,
                    'department': departamento, 'academic_background': historialAcademico, 'labor_experience': experienciaLaboral, 'pass_':pass_}
        return dictDatos

    def registrarMT(self):
        global clienteSocket
        #print "En registrarLT", type(self.comboSexo)
        datos_ = self.recuperarDatos()
        
        reintentar = False
        if datos_ != 'error':
            datos = {'funcion':'insertarMT', 'parametros': datos_}
            m = clienteSocket.enviarMensaje(datos)
            res = None
            if m != 'error':
                res = clienteSocket.recibirRespuesta(False)
                #print "Respuesta de registroLT", res
                if 'ok' in res:
                    msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Registro exitoso"),_fromUtf8("Su suscripción ha sido enviada"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                    self.close()
                else:
                    msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("Su suscripción no pudo ser enviada"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            else:
                print "Error al enviar el mensaje"
                sys.exit()


class VentanaRegistroLT(QtGui.QFrame):
    def __init__(self):
        super(VentanaRegistroLT, self).__init__()
        self.setupUi(self)


    def setupUi(self, VentanaRegistroLT):
        VentanaRegistroLT.setObjectName(_fromUtf8("VentanaRegistroLT"))
        VentanaRegistroLT.resize(727, 611)
        VentanaRegistroLT.setStyleSheet(_fromUtf8(""))
        VentanaRegistroLT.setFrameShape(QtGui.QFrame.StyledPanel)
        VentanaRegistroLT.setFrameShadow(QtGui.QFrame.Raised)
        self.tabWidget = QtGui.QTabWidget(VentanaRegistroLT)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 721, 481))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.etiquetaNombres = QtGui.QLabel(self.tab)
        self.etiquetaNombres.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.etiquetaNombres.setObjectName(_fromUtf8("etiquetaNombres"))
        self.etiquetaApellidos = QtGui.QLabel(self.tab)
        self.etiquetaApellidos.setGeometry(QtCore.QRect(390, 30, 81, 16))
        self.etiquetaApellidos.setObjectName(_fromUtf8("etiquetaApellidos"))
        self.etiquetaID = QtGui.QLabel(self.tab)
        self.etiquetaID.setGeometry(QtCore.QRect(20, 110, 141, 16))
        self.etiquetaID.setObjectName(_fromUtf8("etiquetaID"))
        self.etiquetaCorreo = QtGui.QLabel(self.tab)
        self.etiquetaCorreo.setGeometry(QtCore.QRect(390, 110, 61, 16))
        self.etiquetaCorreo.setObjectName(_fromUtf8("etiquetaCorreo"))
        self.etiquetaTel = QtGui.QLabel(self.tab)
        self.etiquetaTel.setGeometry(QtCore.QRect(20, 190, 71, 16))
        self.etiquetaTel.setObjectName(_fromUtf8("etiquetaTel"))
        self.etiquetaDir = QtGui.QLabel(self.tab)
        self.etiquetaDir.setGeometry(QtCore.QRect(390, 190, 81, 16))
        self.etiquetaDir.setObjectName(_fromUtf8("etiquetaDir"))
        self.campoNombre = QtGui.QLineEdit(self.tab)
        self.campoNombre.setGeometry(QtCore.QRect(20, 60, 311, 23))
        self.campoNombre.setObjectName(_fromUtf8("campoNombre"))
        self.campoApellidos = QtGui.QLineEdit(self.tab)
        self.campoApellidos.setGeometry(QtCore.QRect(390, 60, 301, 23))
        self.campoApellidos.setObjectName(_fromUtf8("campoApellidos"))
        self.campoID = QtGui.QLineEdit(self.tab)
        self.campoID.setGeometry(QtCore.QRect(20, 140, 311, 23))
        self.campoID.setObjectName(_fromUtf8("campoID"))
        self.campoCorreo = QtGui.QLineEdit(self.tab)
        self.campoCorreo.setGeometry(QtCore.QRect(390, 140, 311, 23))
        self.campoCorreo.setText(_fromUtf8(""))
        self.campoCorreo.setObjectName(_fromUtf8("campoCorreo"))
        self.campoTel = QtGui.QLineEdit(self.tab)
        self.campoTel.setGeometry(QtCore.QRect(20, 220, 311, 23))
        self.campoTel.setObjectName(_fromUtf8("campoTel"))
        self.campoDir = QtGui.QLineEdit(self.tab)
        self.campoDir.setGeometry(QtCore.QRect(380, 220, 311, 23))
        self.campoDir.setObjectName(_fromUtf8("campoDir"))
        self.etiquetaSexo = QtGui.QLabel(self.tab)
        self.etiquetaSexo.setGeometry(QtCore.QRect(20, 270, 71, 16))
        self.etiquetaSexo.setObjectName(_fromUtf8("etiquetaSexo"))
        self.etiquetaFecha = QtGui.QLabel(self.tab)
        self.etiquetaFecha.setGeometry(QtCore.QRect(380, 270, 131, 16))
        self.etiquetaFecha.setObjectName(_fromUtf8("etiquetaFecha"))
        self.dateEdit = QtGui.QDateEdit(self.tab)
        self.dateEdit.setGeometry(QtCore.QRect(380, 300, 110, 29))
        self.dateEdit.setDate(QtCore.QDate(2015, 1, 1))
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(7999, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEdit.setMinimumDate(QtCore.QDate(1920, 1, 1))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.etiquetaEstadoCivil = QtGui.QLabel(self.tab)
        self.etiquetaEstadoCivil.setGeometry(QtCore.QRect(20, 350, 101, 16))
        self.etiquetaEstadoCivil.setObjectName(_fromUtf8("etiquetaEstadoCivil"))
        self.comboEstadosCiviles = QtGui.QComboBox(self.tab)
        self.comboEstadosCiviles.setGeometry(QtCore.QRect(20, 380, 101, 25))
        self.comboEstadosCiviles.setModelColumn(0)
        self.comboEstadosCiviles.setObjectName(_fromUtf8("comboEstadosCiviles"))
        self.comboEstadosCiviles.addItem(_fromUtf8(""))
        self.comboEstadosCiviles.addItem(_fromUtf8(""))
        self.comboEstadosCiviles.addItem(_fromUtf8(""))
        self.comboEstadosCiviles.addItem(_fromUtf8(""))
        self.comboSexo = QtGui.QComboBox(self.tab)
        self.comboSexo.setGeometry(QtCore.QRect(20, 300, 311, 23))
        self.comboSexo.setObjectName(_fromUtf8("comboSexo"))
        self.comboSexo.setModelColumn(0)
        self.comboSexo.addItem(_fromUtf8(""))
        self.comboSexo.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.etiquetaSede = QtGui.QLabel(self.tab_2)
        self.etiquetaSede.setGeometry(QtCore.QRect(330, 30, 171, 16))
        self.etiquetaSede.setObjectName(_fromUtf8("etiquetaSede"))
        self.etiquetaInstitucion = QtGui.QLabel(self.tab_2)
        self.etiquetaInstitucion.setGeometry(QtCore.QRect(20, 30, 211, 16))
        self.etiquetaInstitucion.setObjectName(_fromUtf8("etiquetaInstitucion"))
        self.etiquetaGrado = QtGui.QLabel(self.tab_2)
        self.etiquetaGrado.setGeometry(QtCore.QRect(20, 80, 54, 15))
        self.etiquetaGrado.setObjectName(_fromUtf8("etiquetaGrado"))
        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(20, 140, 54, 15))
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.etiquetaSecEd = QtGui.QLabel(self.tab_2)
        self.etiquetaSecEd.setGeometry(QtCore.QRect(320, 130, 251, 16))
        self.etiquetaSecEd.setObjectName(_fromUtf8("etiquetaSecEd"))
        self.etiquetaMunicipio = QtGui.QLabel(self.tab_2)
        self.etiquetaMunicipio.setGeometry(QtCore.QRect(320, 80, 91, 16))
        self.etiquetaMunicipio.setObjectName(_fromUtf8("etiquetaMunicipio"))
        self.etiquetaArea = QtGui.QLabel(self.tab_2)
        self.etiquetaArea.setGeometry(QtCore.QRect(20, 140, 211, 16))
        self.etiquetaArea.setObjectName(_fromUtf8("etiquetaArea"))
        self.etiquetaOtro = QtGui.QLabel(self.tab_2)
        self.etiquetaOtro.setGeometry(QtCore.QRect(20, 250, 31, 16))
        self.etiquetaOtro.setObjectName(_fromUtf8("etiquetaOtro"))
        self.campoOtro = QtGui.QLineEdit(self.tab_2)
        self.campoOtro.setGeometry(QtCore.QRect(60, 250, 161, 23))
        self.campoOtro.setObjectName(_fromUtf8("campoOtro"))
        self.campoSede = QtGui.QLineEdit(self.tab_2)
        self.campoSede.setGeometry(QtCore.QRect(20, 50, 261, 23))
        self.campoSede.setObjectName(_fromUtf8("campoSede"))
        self.campoInstitucion = QtGui.QLineEdit(self.tab_2)
        self.campoInstitucion.setGeometry(QtCore.QRect(320, 50, 291, 23))
        self.campoInstitucion.setObjectName(_fromUtf8("campoInstitucion"))
        self.campoGrado = QtGui.QLineEdit(self.tab_2)
        self.campoGrado.setGeometry(QtCore.QRect(20, 100, 261, 23))
        self.campoGrado.setObjectName(_fromUtf8("campoGrado"))
        self.campoSecEdu = QtGui.QLineEdit(self.tab_2)
        self.campoSecEdu.setGeometry(QtCore.QRect(320, 150, 281, 23))
        self.campoSecEdu.setObjectName(_fromUtf8("campoSecEdu"))
        self.campoMunicipio = QtGui.QLineEdit(self.tab_2)
        self.campoMunicipio.setGeometry(QtCore.QRect(320, 100, 291, 23))
        self.campoMunicipio.setObjectName(_fromUtf8("campoMunicipio"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 160, 271, 80))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radbtnMatematicas = QtGui.QRadioButton(self.groupBox)
        self.radbtnMatematicas.setGeometry(QtCore.QRect(0, 10, 151, 21))
        self.radbtnMatematicas.setObjectName(_fromUtf8("radbtnMatematicas"))
        self.radbtnCiencias = QtGui.QRadioButton(self.groupBox)
        self.radbtnCiencias.setGeometry(QtCore.QRect(0, 30, 261, 21))
        self.radbtnCiencias.setObjectName(_fromUtf8("radbtnCiencias"))
        self.radbtnLenguaje = QtGui.QRadioButton(self.groupBox)
        self.radbtnLenguaje.setGeometry(QtCore.QRect(0, 50, 95, 21))
        self.radbtnLenguaje.setObjectName(_fromUtf8("radbtnLenguaje"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(30, 350, 141, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.scrollArea_2 = QtGui.QScrollArea(self.tab_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(180, 300, 471, 111))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 469, 109))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.textEdit = QtGui.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(180, 300, 471, 111))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.etiquetaDep = QtGui.QLabel(self.tab_2)
        self.etiquetaDep.setGeometry(QtCore.QRect(320, 180, 251, 16))
        self.etiquetaDep.setObjectName(_fromUtf8("etiquetaDep"))
        self.comboDep = QtGui.QComboBox(self.tab_2)
        self.comboDep.setGeometry(QtCore.QRect(320, 200, 121, 25))
        self.comboDep.setObjectName(_fromUtf8("comboDep"))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.comboDep.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.etiquetaExp = QtGui.QLabel(self.tab_3)
        self.etiquetaExp.setGeometry(QtCore.QRect(10, 80, 151, 17))
        self.etiquetaExp.setObjectName(_fromUtf8("etiquetaExp"))
        self.scrollArea = QtGui.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(210, 40, 461, 141))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 139))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.areaExp = QtGui.QTextEdit(self.tab_3)
        self.areaExp.setGeometry(QtCore.QRect(210, 40, 461, 141))
        self.areaExp.setObjectName(_fromUtf8("areaExp"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.etiquetaTitulo = QtGui.QLabel(VentanaRegistroLT)
        self.etiquetaTitulo.setGeometry(QtCore.QRect(300, 0, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitulo.setFont(font)
        self.etiquetaTitulo.setObjectName(_fromUtf8("etiquetaTitulo"))
        self.etiquetaSubTit1 = QtGui.QLabel(VentanaRegistroLT)
        self.etiquetaSubTit1.setGeometry(QtCore.QRect(70, 20, 581, 20))
        self.etiquetaSubTit1.setObjectName(_fromUtf8("etiquetaSubTit1"))
        self.etiquetaSubTit2 = QtGui.QLabel(VentanaRegistroLT)
        self.etiquetaSubTit2.setGeometry(QtCore.QRect(310, 40, 101, 16))
        self.etiquetaSubTit2.setStyleSheet(_fromUtf8("color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));"))
        self.etiquetaSubTit2.setObjectName(_fromUtf8("etiquetaSubTit2"))
        self.botonEnviar = QtGui.QPushButton(VentanaRegistroLT)
        self.botonEnviar.setGeometry(QtCore.QRect(170, 570, 91, 24))
        self.botonEnviar.setObjectName(_fromUtf8("botonEnviar"))
        self.botonSalir = QtGui.QPushButton(VentanaRegistroLT)
        self.botonSalir.setGeometry(QtCore.QRect(410, 570, 91, 24))
        self.botonSalir.setObjectName(_fromUtf8("botonSalir"))

        #print "en setupUi", type(self.comboSexo)
        self.retranslateUi(VentanaRegistroLT)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VentanaRegistroLT)
        QtCore.QObject.connect(self.botonSalir, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaRegistroLT.close)
        QtCore.QObject.connect(self.botonEnviar, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaRegistroLT.registrarLT)

    def retranslateUi(self, VentanaRegistroLT):
        VentanaRegistroLT.setWindowTitle(_translate("VentanaRegistroLT", "Frame", None))
        self.etiquetaNombres.setText(_translate("VentanaRegistroLT", "Nombres *", None))
        self.etiquetaApellidos.setText(_translate("VentanaRegistroLT", "Apellidos *", None))
        self.etiquetaID.setText(_translate("VentanaRegistroLT", "Num. Identificación *", None))
        self.etiquetaCorreo.setText(_translate("VentanaRegistroLT", "Correo *", None))
        self.etiquetaTel.setText(_translate("VentanaRegistroLT", "Teléfono *", None))
        self.etiquetaDir.setText(_translate("VentanaRegistroLT", "Dirección *", None))
        self.etiquetaSexo.setText(_translate("VentanaRegistroLT", "Sexo *", None))
        self.etiquetaFecha.setText(_translate("VentanaRegistroLT", "Fecha Nacimiento *", None))
        self.etiquetaEstadoCivil.setText(_translate("VentanaRegistroLT", "Estado civil *", None))
        self.comboEstadosCiviles.setItemText(0, _translate("VentanaRegistroLT", "Soltero", None))
        self.comboEstadosCiviles.setItemText(1, _translate("VentanaRegistroLT", "Casado", None))
        self.comboEstadosCiviles.setItemText(2, _translate("VentanaRegistroLT", "Viudo", None))
        self.comboEstadosCiviles.setItemText(3, _translate("VentanaRegistroLT", "Union Libre", None))
        self.comboSexo.setItemText(0, _translate("VentanaRegistroLT", "Masculino", None))
        self.comboSexo.setItemText(1, _translate("VentanaRegistroLT", "Femenino", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("VentanaRegistroLT", "Información Personal", None))
        self.etiquetaSede.setText(_translate("VentanaRegistroLT", "Sede a la que pertenece *", None))
        self.etiquetaInstitucion.setText(_translate("VentanaRegistroLT", "Institución a la que pertenece *", None))
        self.etiquetaGrado.setText(_translate("VentanaRegistroLT", "Grado *", None))
        self.etiquetaSecEd.setText(_translate("VentanaRegistroLT", "Secretaría de Educación *", None))
        self.etiquetaMunicipio.setText(_translate("VentanaRegistroLT", "Municipio *", None))
        self.etiquetaArea.setText(_translate("VentanaRegistroLT", "Área a la cual se va a inscribir *", None))
        self.etiquetaOtro.setText(_translate("VentanaRegistroLT", "Otro:", None))
        self.radbtnMatematicas.setText(_translate("VentanaRegistroLT", " Matemáticas", None))
        self.radbtnCiencias.setText(_translate("VentanaRegistroLT", "Ciencias Naturales y Ed. Ambiental    ", None))
        self.radbtnLenguaje.setText(_translate("VentanaRegistroLT", "Lenguaje", None))
        self.label.setText(_translate("VentanaRegistroLT", "Historial Académico", None))
        self.etiquetaDep.setText(_translate("VentanaRegistroLT", "Departamento *", None))
        self.comboDep.setItemText(0, _translate("VentanaRegistroLT", "Valle del Cauca", None))
        self.comboDep.setItemText(1, _translate("VentanaRegistroLT", "Nariño", None))
        self.comboDep.setItemText(2, _translate("VentanaRegistroLT", "Tolima", None))
        self.comboDep.setItemText(3, _translate("VentanaRegistroLT", "Cauca", None))
        self.comboDep.setItemText(4, _translate("VentanaRegistroLT", "Huila", None))
        self.comboDep.setItemText(5, _translate("VentanaRegistroLT", "Caqueta", None))
        self.comboDep.setItemText(6, _translate("VentanaRegistroLT", "Putumayo", None))
        self.comboDep.setItemText(7, _translate("VentanaRegistroLT", "Amazonas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("VentanaRegistroLT", "Información Profesional", None))
        self.etiquetaExp.setText(_translate("VentanaRegistroLT", "Experiencia Laboral:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("VentanaRegistroLT", "Adicional", None))
        self.etiquetaTitulo.setText(_translate("VentanaRegistroLT", "CIER-SUR", None))
        self.etiquetaSubTit1.setText(_translate("VentanaRegistroLT", "Formulario de inscripción de profesores al programa de formación CREA-TIC / CIER-SUR", None))
        self.etiquetaSubTit2.setText(_translate("VentanaRegistroLT", "(*) Obligatorio", None))
        self.botonEnviar.setText(_translate("VentanaRegistroLT", "Enviar", None))
        self.botonSalir.setText(_translate("VentanaRegistroLT", "Salir", None))
        #print "en retranslateUi ", type(self.comboSexo)

    def recuperarDatos(self):
        index = self.comboSexo.currentIndex()
        sex = ''
        if index == 0:
            sex = 'M'
        else:
            sex = 'F'
        #sexo = self.comboSexo().currentText()
        nombres = str(self.campoNombre.text())
        if nombres == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo Nombres es obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        apellidos = str(self.campoApellidos.text())
        if apellidos == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo Apellidos es obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        id_ = str(self.campoID.text())
        if id_ == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo Identificación es obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        correo = str(self.campoCorreo.text())
        if correo == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo correo es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        tel = str(self.campoTel.text())
        if tel == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo telefono es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        direccion = str(self.campoDir.text())
        if direccion == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo direccion es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        fechaNacimiento = str(self.dateEdit.date().toString("yyyy.MM.dd"))
        print fechaNacimiento
        estadoCivil = str(self.comboEstadosCiviles.currentText())
        institucion = str(self.campoInstitucion.text())
        if institucion == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo institución es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        grado = str(self.campoGrado.text())
        if grado == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo grado es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        sede = str(self.campoSede.text())
        municipio = str(self.campoMunicipio.text())
        if municipio == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo municipio es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        secretaria = str(self.campoSecEdu.text())
        if secretaria == '':
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("El campo Secretaría es Obligatorio"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return 'error'
        departamento = str(self.comboDep.currentText())
        area = ''
        if self.radbtnMatematicas.isChecked():
            area = 'Matemáticas'
        elif self.radbtnLenguaje.isChecked():
            area = 'Lenguaje'
        elif self.radbtnCiencias.isChecked():
            area = 'Ciencias'
        else:
            area = str(self.campoOtro.text())
        historialAcademico = ''
        experienciaLaboral = ''
        try:
            txt1 = str(self.textEdit.toPlainText())
            historialAcademico = txt1.split("\n")
            #historialAcademico = txt1.split(",")
            txt2 = str(self.areaExp.toPlainText())
            #text2 = txt2.replace("\n", "")
            experienciaLaboral = txt2.split("\n")
        except Exception as ex:
            print ex
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("La experiencia laboral y \n el historial academico deben tener todos sus items separados por comas"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

        pass_ = nombres[0] + id_ + apellidos[0]

        dictDatos = {'first_name':nombres, 'last_name':apellidos, 'id': id_, 'email': correo, 'tel_num':tel, 'is_active': False,
                    'address': direccion, 'sex': sex, 'birth_date': fechaNacimiento, 'marital_status': estadoCivil,
                    'institution': institucion, 'grade': grado, 'city':municipio, 'area':area, 'secretariat':secretaria,
                    'department': departamento, 'academic_background': historialAcademico, 'labor_experience': experienciaLaboral, 'pass_':pass_}
        return dictDatos

    def registrarLT(self):
        global clienteSocket
        #print "En registrarLT", type(self.comboSexo)
        datos = self.recuperarDatos()
        
        reintentar = False
        if datos != 'error':
            datos = {'funcion':'insertarLT', 'parametros': datos}
            m = clienteSocket.enviarMensaje(datos)
            res = None
            if m != 'error':
                res = clienteSocket.recibirRespuesta(False)
                print "Respuesta de registroLT", res
                if 'ok' in res:
                    msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Registro exitoso"),_fromUtf8("Su suscripción ha sido enviada"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                    self.close()
                else:
                    msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("Su suscripción no pudo ser enviada"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            else:
                print "Error al enviar el mensaje"
                sys.exit()


    


class VentanaLogin(QtGui.QFrame):

    def __init__(self):
        global clienteSocket
        super(VentanaLogin, self).__init__()
        self.ventanaRegLT = VentanaRegistroLT()
        self.ventanaOpAdm = VentanaOpcionesAdm()
        self.ventanaOpLT = VentanaRevisarNotas()
        self.ventanaOpMT = VentanaAsignarNotas()
        self.ventanaOpCoor = VentanaOpcionesRegistroCoor();
        self.setupUi(self)
        try:
            clienteSocket.conectar()
            msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("Conexion con el servidor establecida"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        except Exception as ex:
            clienteSocket.desconectar()
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("No hay conexion con el servidor"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

    def setupUi(self, VentanaLogin):
        VentanaLogin.setObjectName(_fromUtf8("VentanaLogin"))
        VentanaLogin.resize(516, 218)
        VentanaLogin.setFrameShape(QtGui.QFrame.StyledPanel)
        VentanaLogin.setFrameShadow(QtGui.QFrame.Raised)
        self.boton_ingresar = QtGui.QPushButton(VentanaLogin)
        self.boton_ingresar.setGeometry(QtCore.QRect(210, 150, 91, 24))
        self.boton_ingresar.setObjectName(_fromUtf8("boton_ingresar"))
        self.boton_salir = QtGui.QPushButton(VentanaLogin)
        self.boton_salir.setGeometry(QtCore.QRect(340, 150, 91, 24))
        self.boton_salir.setObjectName(_fromUtf8("boton_salir"))
        self.campo_usuario = QtGui.QLineEdit(VentanaLogin)
        self.campo_usuario.setGeometry(QtCore.QRect(110, 60, 211, 23))
        self.campo_usuario.setObjectName(_fromUtf8("campo_usuario"))
        self.campo_pass = QtGui.QLineEdit(VentanaLogin)
        self.campo_pass.setGeometry(QtCore.QRect(110, 100, 211, 23))
        self.campo_pass.setText(_fromUtf8(""))
        self.campo_pass.setEchoMode(QtGui.QLineEdit.Password)
        self.campo_pass.setObjectName(_fromUtf8("campo_pass"))
        self.etiqueta_usuario = QtGui.QLabel(VentanaLogin)
        self.etiqueta_usuario.setGeometry(QtCore.QRect(20, 60, 54, 15))
        self.etiqueta_usuario.setObjectName(_fromUtf8("etiqueta_usuario"))
        self.etiqueta_pass = QtGui.QLabel(VentanaLogin)
        self.etiqueta_pass.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.etiqueta_pass.setObjectName(_fromUtf8("etiqueta_pass"))
        self.etiqueta_titulo = QtGui.QLabel(VentanaLogin)
        self.etiqueta_titulo.setGeometry(QtCore.QRect(170, 10, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_titulo.setFont(font)
        self.etiqueta_titulo.setObjectName(_fromUtf8("etiqueta_titulo"))
        self.comboBox = QtGui.QComboBox(VentanaLogin)
        self.comboBox.setGeometry(QtCore.QRect(360, 60, 121, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.botonInscribir = QtGui.QPushButton(VentanaLogin)
        self.botonInscribir.setGeometry(QtCore.QRect(20, 150, 151, 27))
        self.botonInscribir.setObjectName(_fromUtf8("botonInscribir"))

        self.retranslateUi()
        QtCore.QObject.connect(self.boton_salir, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaLogin.close)
        QtCore.QObject.connect(self.boton_ingresar, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaLogin.ingresarAlSistema)
        QtCore.QObject.connect(self.botonInscribir, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaLogin.mostrarRegLT)
        QtCore.QMetaObject.connectSlotsByName(VentanaLogin)

    def ingresarAlSistema(self):
        global clienteSocket
        if clienteSocket.hayConexion:
            usr = self.campo_usuario.text()
            pass_ = self.campo_pass.text()
            if (usr == '' or  pass_ == '' or usr is None or pass_ is None):
                msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error"),_fromUtf8("Los campos no pueden estar vacios"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                #dialogo = QtGui.QErrorMessage(self)
                #dialogo.showMessage(_fromUtf8("Los campos no pueden estar vacios"))
            else:
                ct = self.comboBox.currentText()
                if ct == "Administrator":
                    datos = {'funcion':'consultarAdmPassUsr', 
                             'parametros': {'usr': usr, 'pass': pass_}}
                    m = clienteSocket.enviarMensaje(datos)
                    if m == 'ok':
                        res = clienteSocket.recibirRespuesta(False)
                        msgBox = QtGui.QMessageBox;
                        print "Respuesta ", res[2]
                        if res[2] == '1':
                            msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Bienvenido "),_fromUtf8("Ingreso exitoso " + usr), QtGui.QMessageBox.Yes, QtGui.QMessageBox.Yes)
                            self.ventanaOpAdm.show()
                            self.hide()
                        else:
                            msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("Usuario " + usr + "No encontrado \n Por favor revise su usuario o contraseña e intente nuevamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                            #msgBox.exec_()
                    elif m == 'error':
                        msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("Usuario " + usr + "No encontrado \n Por favor revise su usuario o contraseña e intente nuevamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                elif ct == "Coordinator":
                    datos = {'funcion':'consultarCoorPassUsr','parametros':{'usr':usr, 'pass':pass_}}
                    m = clienteSocket.enviarMensaje(datos)
                    if m == 'ok':
                        res = clienteSocket.recibirRespuesta(False)
                        msgBox = QtGui.QMessageBox;
                        print "Respuesta", res[2]
                        if res[2] == '1':
                            msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Bienvenido "),_fromUtf8("Ingreso exitoso " + usr), QtGui.QMessageBox.Yes, QtGui.QMessageBox.Yes)
                            self.ventanaOpCoor.show()
                            self.hide()
                        else:
                            msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("Usuario " + usr + "No encontrado \n Por favor revise su usuario o contraseña e intente nuevamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                elif ct == "Master Teacher":
                    datos = {'funcion':'consultarMTPassUsr','parametros':{'usr':usr, 'pass':pass_}}
                    m = clienteSocket.enviarMensaje(datos)
                    if m == 'ok':
                        res = clienteSocket.recibirRespuesta(False)
                        msgBox = QtGui.QMessageBox;
                        print "Respuesta", res[2]
                        if res[2] == '1':
                            msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Bienvenido "),_fromUtf8("Ingreso exitoso " + usr), QtGui.QMessageBox.Yes, QtGui.QMessageBox.Yes)
                            self.hide()
                            self.ventanaOpMT.show()
                        else:
                            msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("Usuario " + usr + "No encontrado \n Por favor revise su usuario o contraseña e intente nuevamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                elif ct == "Leader Teacher":
                    datos = {'funcion':'consultarLTPassUsr','parametros':{'usr':usr, 'pass':pass_}}
                    m = clienteSocket.enviarMensaje(datos)
                    if m == 'ok':
                        res = clienteSocket.recibirRespuesta(False)
                        msgBox = QtGui.QMessageBox;
                        print "Respuesta", res[2]
                        if res[2] == '1':
                            msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Bienvenido "),_fromUtf8("Ingreso exitoso " + usr), QtGui.QMessageBox.Yes, QtGui.QMessageBox.Yes)
                            self.hide()
                            self.ventanaOpLT.show()
                        else:
                            msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("Usuario " + usr + "No encontrado \n Por favor revise su usuario o contraseña e intente nuevamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        else:
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("No hay conexion con el servidor"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)


            



    def mostrarRegLT(self):
        self.ventanaRegLT.show()

    def retranslateUi(self):
        self.setWindowTitle(_translate("VentanaLogin", "Frame", None))
        self.boton_ingresar.setText(_translate("VentanaLogin", "Ingresar", None))
        self.boton_salir.setText(_translate("VentanaLogin", "Salir", None))
        self.etiqueta_usuario.setText(_translate("VentanaLogin", "Usuario:", None))
        self.etiqueta_pass.setText(_translate("VentanaLogin", "Contraseña:", None))
        self.etiqueta_titulo.setText(_translate("VentanaLogin", "INGRESAR AL SISTEMA", None))
        self.comboBox.setItemText(0, _translate("VentanaLogin", "Administrator", None))
        self.comboBox.setItemText(1, _translate("VentanaLogin", "Coordinator", None))
        self.comboBox.setItemText(2, _translate("VentanaLogin", "Master Teacher", None))
        self.comboBox.setItemText(3, _translate("VentanaLogin", "Leader Teacher", None))
        self.botonInscribir.setText(_translate("VentanaLogin", "Inscripciones Cursos", None))






if __name__  == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = VentanaLogin()
    w.show()
    sys.exit(app.exec_())
