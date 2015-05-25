# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroAdm-IGU.ui'
#
# Created: Sun May 24 18:01:32 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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
        QtCore.QMetaObject.connectSlotsByName(VentanaRegistroAdm)

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

