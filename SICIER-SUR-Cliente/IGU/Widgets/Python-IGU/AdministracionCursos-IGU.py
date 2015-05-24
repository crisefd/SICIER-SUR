# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdministracionCursos-IGU.ui'
#
# Created: Sun May 24 14:09:02 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

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

class VentanaAdministrarCursos(QtGui.QFrame):
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
        self.etiquetaBuscarDescripcionCurso = QtGui.QLabel(self.Buscar)
        self.etiquetaBuscarDescripcionCurso.setGeometry(QtCore.QRect(20, 60, 91, 17))
        self.etiquetaBuscarDescripcionCurso.setObjectName(_fromUtf8("etiquetaBuscarDescripcionCurso"))
        self.etiquetaBuscarInicioCurso = QtGui.QLabel(self.Buscar)
        self.etiquetaBuscarInicioCurso.setGeometry(QtCore.QRect(20, 90, 66, 17))
        self.etiquetaBuscarInicioCurso.setObjectName(_fromUtf8("etiquetaBuscarInicioCurso"))
        self.etiquetaBuscarFinCurso = QtGui.QLabel(self.Buscar)
        self.etiquetaBuscarFinCurso.setGeometry(QtCore.QRect(20, 120, 66, 17))
        self.etiquetaBuscarFinCurso.setObjectName(_fromUtf8("etiquetaBuscarFinCurso"))
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
            if id_curso != '':
                datos = {'funcion':'consultarCursoPorID', 'parametros': {'id':id_curso}}
                clienteSocket.enviarMensaje(datos)
                ls = clienteSocket.recibirRespuesta(True)
                for item in ls:
                    str_item = ""
                    for cad in item:
                        str_item += cad + " "
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
        self.etiquetaBuscarDescripcionCurso.setText(_translate("VentanaAdministrarCursos", "Descripcion", None))
        self.etiquetaBuscarInicioCurso.setText(_translate("VentanaAdministrarCursos", "Inicio", None))
        self.etiquetaBuscarFinCurso.setText(_translate("VentanaAdministrarCursos", "Fin", None))
        self.etiquetaBuscarActividadesCurso.setText(_translate("VentanaAdministrarCursos", "Resultados", None))
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