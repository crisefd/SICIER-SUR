## -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login-IGU.ui'
#
# Created: Sun Apr 26 09:51:56 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

import sys
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


class VentanaAdministrarCursos(QtGui.QFrame):
    def __init__(self):
        super(VentanaAdministrarCursos, self).__init__()
        self.setupUi(self)

    def setupUi(self, VentanaAdministrarCursos):
        VentanaAdministrarCursos.setObjectName(_fromUtf8("VentanaAdministrarCursos"))
        VentanaAdministrarCursos.resize(554, 370)
        self.tabWidget = QtGui.QTabWidget(VentanaAdministrarCursos)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 551, 291))
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
        self.etiquetaBuscarDescripcionCurso = QtGui.QLabel(self.Buscar)
        self.etiquetaBuscarDescripcionCurso.setGeometry(QtCore.QRect(20, 60, 91, 17))
        self.etiquetaBuscarDescripcionCurso.setObjectName(_fromUtf8("etiquetaBuscarDescripcionCurso"))
        self.etiquetaBuscarInicioCurso = QtGui.QLabel(self.Buscar)
        self.etiquetaBuscarInicioCurso.setGeometry(QtCore.QRect(20, 90, 66, 17))
        self.etiquetaBuscarInicioCurso.setObjectName(_fromUtf8("etiquetaBuscarInicioCurso"))
        self.etiquetaBuscarFinCurso = QtGui.QLabel(self.Buscar)
        self.etiquetaBuscarFinCurso.setGeometry(QtCore.QRect(20, 120, 66, 17))
        self.etiquetaBuscarFinCurso.setObjectName(_fromUtf8("etiquetaBuscarFinCurso"))
        self.botonBuscarLimparCurso = QtGui.QPushButton(self.Buscar)
        self.botonBuscarLimparCurso.setGeometry(QtCore.QRect(20, 210, 131, 27))
        self.botonBuscarLimparCurso.setObjectName(_fromUtf8("botonBuscarLimparCurso"))
        self.campoBuscarDescripcionCurso = QtGui.QLineEdit(self.Buscar)
        self.campoBuscarDescripcionCurso.setGeometry(QtCore.QRect(110, 50, 113, 27))
        self.campoBuscarDescripcionCurso.setObjectName(_fromUtf8("campoBuscarDescripcionCurso"))
        self.campoBuscarInicioCurso = QtGui.QLineEdit(self.Buscar)
        self.campoBuscarInicioCurso.setGeometry(QtCore.QRect(110, 80, 113, 27))
        self.campoBuscarInicioCurso.setObjectName(_fromUtf8("campoBuscarInicioCurso"))
        self.campoBuscarFinCurso = QtGui.QLineEdit(self.Buscar)
        self.campoBuscarFinCurso.setGeometry(QtCore.QRect(110, 110, 113, 27))
        self.campoBuscarFinCurso.setObjectName(_fromUtf8("campoBuscarFinCurso"))
        self.etiquetaBuscarActividadesCurso = QtGui.QLabel(self.Buscar)
        self.etiquetaBuscarActividadesCurso.setGeometry(QtCore.QRect(260, 30, 161, 17))
        self.etiquetaBuscarActividadesCurso.setObjectName(_fromUtf8("etiquetaBuscarActividadesCurso"))
        self.listaBuscarActividadescurso = QtGui.QListWidget(self.Buscar)
        self.listaBuscarActividadescurso.setGeometry(QtCore.QRect(260, 50, 256, 192))
        self.listaBuscarActividadescurso.setObjectName(_fromUtf8("listaBuscarActividadescurso"))
        self.tabWidget.addTab(self.Buscar, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.campoBorrarCurso = QtGui.QLineEdit(self.tab_2)
        self.campoBorrarCurso.setGeometry(QtCore.QRect(90, 40, 113, 27))
        self.campoBorrarCurso.setObjectName(_fromUtf8("campoBorrarCurso"))
        self.etiquetaBorrarCurso = QtGui.QLabel(self.tab_2)
        self.etiquetaBorrarCurso.setGeometry(QtCore.QRect(20, 50, 66, 17))
        self.etiquetaBorrarCurso.setObjectName(_fromUtf8("etiquetaBorrarCurso"))
        self.BotonBorrarCurso = QtGui.QPushButton(self.tab_2)
        self.BotonBorrarCurso.setGeometry(QtCore.QRect(240, 40, 98, 27))
        self.BotonBorrarCurso.setObjectName(_fromUtf8("BotonBorrarCurso"))
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
        self.campoCrearActividadCurso = QtGui.QLineEdit(self.tab_3)
        self.campoCrearActividadCurso.setGeometry(QtCore.QRect(200, 160, 113, 27))
        self.campoCrearActividadCurso.setObjectName(_fromUtf8("campoCrearActividadCurso"))
        self.etiquetaCrearActividadCurso = QtGui.QLabel(self.tab_3)
        self.etiquetaCrearActividadCurso.setGeometry(QtCore.QRect(40, 170, 131, 17))
        self.etiquetaCrearActividadCurso.setObjectName(_fromUtf8("etiquetaCrearActividadCurso"))
        self.botonCrearAgregarActividadCurso = QtGui.QPushButton(self.tab_3)
        self.botonCrearAgregarActividadCurso.setGeometry(QtCore.QRect(330, 160, 81, 27))
        self.botonCrearAgregarActividadCurso.setObjectName(_fromUtf8("botonCrearAgregarActividadCurso"))
        self.botonCrearCurso = QtGui.QPushButton(self.tab_3)
        self.botonCrearCurso.setGeometry(QtCore.QRect(80, 220, 98, 27))
        self.botonCrearCurso.setObjectName(_fromUtf8("botonCrearCurso"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.campoEditarIdcurso = QtGui.QLineEdit(self.tab)
        self.campoEditarIdcurso.setGeometry(QtCore.QRect(170, 40, 113, 27))
        self.campoEditarIdcurso.setObjectName(_fromUtf8("campoEditarIdcurso"))
        self.campoEditardescripcioncurso = QtGui.QLineEdit(self.tab)
        self.campoEditardescripcioncurso.setGeometry(QtCore.QRect(170, 70, 113, 27))
        self.campoEditardescripcioncurso.setObjectName(_fromUtf8("campoEditardescripcioncurso"))
        self.campoEditarActividadcurso = QtGui.QLineEdit(self.tab)
        self.campoEditarActividadcurso.setGeometry(QtCore.QRect(170, 160, 113, 27))
        self.campoEditarActividadcurso.setObjectName(_fromUtf8("campoEditarActividadcurso"))
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
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(30, 170, 131, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.botonEditarAgregarActividadCurso = QtGui.QPushButton(self.tab)
        self.botonEditarAgregarActividadCurso.setGeometry(QtCore.QRect(310, 160, 81, 27))
        self.botonEditarAgregarActividadCurso.setObjectName(_fromUtf8("botonEditarAgregarActividadCurso"))
        self.botonEditarCurso = QtGui.QPushButton(self.tab)
        self.botonEditarCurso.setGeometry(QtCore.QRect(110, 210, 98, 27))
        self.botonEditarCurso.setObjectName(_fromUtf8("botonEditarCurso"))
        self.botonEditarQuitarActividadCurso = QtGui.QPushButton(self.tab)
        self.botonEditarQuitarActividadCurso.setGeometry(QtCore.QRect(400, 160, 98, 27))
        self.botonEditarQuitarActividadCurso.setObjectName(_fromUtf8("botonEditarQuitarActividadCurso"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(VentanaAdministrarCursos)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(VentanaAdministrarCursos)

    def retranslateUi(self, VentanaAdministrarCursos):
        VentanaAdministrarCursos.setWindowTitle(_translate("VentanaAdministrarCursos", "Form", None))
        self.botonBuscarCurso.setText(_translate("VentanaAdministrarCursos", "Buscar", None))
        self.etiquetaBuscarIdCurso.setText(_translate("VentanaAdministrarCursos", "ID", None))
        self.etiquetaBuscarDescripcionCurso.setText(_translate("VentanaAdministrarCursos", "Descripcion", None))
        self.etiquetaBuscarInicioCurso.setText(_translate("VentanaAdministrarCursos", "Inicio", None))
        self.etiquetaBuscarFinCurso.setText(_translate("VentanaAdministrarCursos", "Fin", None))
        self.botonBuscarLimparCurso.setText(_translate("VentanaAdministrarCursos", "Limpiar campos", None))
        self.etiquetaBuscarActividadesCurso.setText(_translate("VentanaAdministrarCursos", "Nombre Actividadades", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Buscar), _translate("VentanaAdministrarCursos", "Buscar", None))
        self.etiquetaBorrarCurso.setText(_translate("VentanaAdministrarCursos", "ID", None))
        self.BotonBorrarCurso.setText(_translate("VentanaAdministrarCursos", "Borrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("VentanaAdministrarCursos", "Borrar", None))
        self.etiquetaCrearIdCurso.setText(_translate("VentanaAdministrarCursos", "ID", None))
        self.etiquetaCrearDescripcionCurso.setText(_translate("VentanaAdministrarCursos", "Descripcion", None))
        self.etiquetaCrearInicioCurso.setText(_translate("VentanaAdministrarCursos", "Inicio", None))
        self.etiquetaCrearFinCurso.setText(_translate("VentanaAdministrarCursos", "Fin", None))
        self.etiquetaCrearActividadCurso.setText(_translate("VentanaAdministrarCursos", "Nombre Actividad", None))
        self.botonCrearAgregarActividadCurso.setText(_translate("VentanaAdministrarCursos", "Agregar", None))
        self.botonCrearCurso.setText(_translate("VentanaAdministrarCursos", "Crear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("VentanaAdministrarCursos", "Crear", None))
        self.label_7.setText(_translate("VentanaAdministrarCursos", "ID", None))
        self.label_8.setText(_translate("VentanaAdministrarCursos", "Descripcion", None))
        self.label_9.setText(_translate("VentanaAdministrarCursos", "Inicio", None))
        self.label_10.setText(_translate("VentanaAdministrarCursos", "Fin", None))
        self.label_11.setText(_translate("VentanaAdministrarCursos", "Nombre Actividad", None))
        self.botonEditarAgregarActividadCurso.setText(_translate("VentanaAdministrarCursos", "Agregar", None))
        self.botonEditarCurso.setText(_translate("VentanaAdministrarCursos", "Editar", None))
        self.botonEditarQuitarActividadCurso.setText(_translate("VentanaAdministrarCursos", "Quitar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("VentanaAdministrarCursos", "Editar", None))

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
            txt1 = txt1.replace("\n", "")
            historialAcademico = txt1.split(",")
            txt2 = str(self.areaExp.toPlainText())
            text2 = txt2.replace("\n", "")
            experienciaLaboral = txt2.split(",")
        except Exception as ex:
            print ex
            msgBox = QtGui.QMessageBox.critical(self, _fromUtf8("Error "),_fromUtf8("La experiencia laboral y \n el historial academico deben tener todos sus items separados por comas"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

        pass_ = nombres[0] + id_ + apellidos[0]

        dictDatos = {'first_name':nombres, 'last_name':apellidos, 'id': id_, 'email': correo, 'tel_num':tel, 'is_active': False,
                    'address': direccion, 'sex': sex, 'birth_date': fechaNacimiento, 'marital_status': estadoCivil,
                    'institution': institucion, 'grade': grado, 'city':municipio, 'area':area, 'secretariat':secretaria,
                    'academic_background': historialAcademico, 'labor_experience': experienciaLaboral, 'pass_':pass_}
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
                res = clienteSocket.recibirRespuesta()
                if res == 'ok':
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
        self.setupUi(self)
        try:
            clienteSocket.conectar()
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
                        res = clienteSocket.recibirRespuesta()
                        msgBox = QtGui.QMessageBox;
                        print "Respuesta ", res[2]
                        if res[2] == '1':
                            msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Bienvenido "),_fromUtf8("Ingreso exitoso " + usr), QtGui.QMessageBox.Yes, QtGui.QMessageBox.Yes)
                            #msgBox.setText(_fromUtf8("Bienvenido " + usr));
                            #msgBox.exec_()
                        else:
                            msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("Usuario " + usr + "No encontrado \n Por favor revise su usuario o contraseña e intente nuevamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                            #msgBox.exec_()
                    elif m == 'error':
                        msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Error "),_fromUtf8("Usuario " + usr + "No encontrado \n Por favor revise su usuario o contraseña e intente nuevamente"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                elif ct == "Coordinator":
                    msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Falta"),_fromUtf8("No implementado"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                    pass
                elif ct == "Master Teacher":
                    msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Falta"),_fromUtf8("No implementado"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                    pass
                elif ct == "Leader Teacher":
                    msgBox = QtGui.QMessageBox.information(self, _fromUtf8("Falta"),_fromUtf8("No implementado"), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                    pass
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
