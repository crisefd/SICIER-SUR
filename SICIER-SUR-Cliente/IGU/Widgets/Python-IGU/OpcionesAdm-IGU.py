# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpcionesAdm-IGU.ui'
#
# Created: Sat May 23 12:33:45 2015
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

class Ui_ventantaOpcionesAdm(object):
    def setupUi(self, ventantaOpcionesAdm):
        ventantaOpcionesAdm.setObjectName(_fromUtf8("ventantaOpcionesAdm"))
        ventantaOpcionesAdm.resize(541, 322)
        ventantaOpcionesAdm.setFrameShape(QtGui.QFrame.StyledPanel)
        ventantaOpcionesAdm.setFrameShadow(QtGui.QFrame.Raised)
        self.etiquetaTitutlo = QtGui.QLabel(ventantaOpcionesAdm)
        self.etiquetaTitutlo.setGeometry(QtCore.QRect(170, 20, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitutlo.setFont(font)
        self.etiquetaTitutlo.setObjectName(_fromUtf8("etiquetaTitutlo"))
        self.botonEditarPerfil = QtGui.QPushButton(ventantaOpcionesAdm)
        self.botonEditarPerfil.setGeometry(QtCore.QRect(60, 90, 151, 27))
        self.botonEditarPerfil.setObjectName(_fromUtf8("botonEditarPerfil"))
        self.botonCerrarSesion = QtGui.QPushButton(ventantaOpcionesAdm)
        self.botonCerrarSesion.setGeometry(QtCore.QRect(410, 20, 98, 27))
        self.botonCerrarSesion.setObjectName(_fromUtf8("botonCerrarSesion"))
        self.botonAdmUsuarios = QtGui.QPushButton(ventantaOpcionesAdm)
        self.botonAdmUsuarios.setGeometry(QtCore.QRect(270, 90, 151, 27))
        self.botonAdmUsuarios.setObjectName(_fromUtf8("botonAdmUsuarios"))
        self.botonReportes = QtGui.QPushButton(ventantaOpcionesAdm)
        self.botonReportes.setGeometry(QtCore.QRect(60, 150, 161, 27))
        self.botonReportes.setObjectName(_fromUtf8("botonReportes"))
        self.botonAdmCursos = QtGui.QPushButton(ventantaOpcionesAdm)
        self.botonAdmCursos.setGeometry(QtCore.QRect(270, 150, 151, 27))
        self.botonAdmCursos.setObjectName(_fromUtf8("botonAdmCursos"))
        self.botonListaBecados = QtGui.QPushButton(ventantaOpcionesAdm)
        self.botonListaBecados.setGeometry(QtCore.QRect(60, 200, 161, 27))
        self.botonListaBecados.setObjectName(_fromUtf8("botonListaBecados"))

        self.retranslateUi(ventantaOpcionesAdm)
        QtCore.QMetaObject.connectSlotsByName(ventantaOpcionesAdm)

    def retranslateUi(self, ventantaOpcionesAdm):
        ventantaOpcionesAdm.setWindowTitle(_translate("ventantaOpcionesAdm", "Opciones Adm", None))
        self.etiquetaTitutlo.setText(_translate("ventantaOpcionesAdm", "¿Qué Desea Hacer?", None))
        self.botonEditarPerfil.setText(_translate("ventantaOpcionesAdm", "Editar Perfil", None))
        self.botonCerrarSesion.setText(_translate("ventantaOpcionesAdm", "Cerrar sesión", None))
        self.botonAdmUsuarios.setText(_translate("ventantaOpcionesAdm", "Administrar Usuarios", None))
        self.botonReportes.setText(_translate("ventantaOpcionesAdm", "Ver Reportes", None))
        self.botonAdmCursos.setText(_translate("ventantaOpcionesAdm", "Administrar Cursos", None))
        self.botonListaBecados.setText(_translate("ventantaOpcionesAdm", "Ingresar Lista Becados", None))

