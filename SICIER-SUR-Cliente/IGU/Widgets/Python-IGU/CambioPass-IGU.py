# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CambioPass-IGU.ui'
#
# Created: Fri May  8 10:34:34 2015
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

class DialogoCambioPass(QtGui.QFrame):

    def __init__(self):
        super(DialogoCambioPass, self).__init__()
        self.setupUi(self)

    def setupUi(self, DialogoCambioPass):
        DialogoCambioPass.setObjectName(_fromUtf8("DialogoCambioPass"))
        DialogoCambioPass.resize(594, 181)
        self.etiquetaPassAnterior = QtGui.QLabel(DialogoCambioPass)
        self.etiquetaPassAnterior.setGeometry(QtCore.QRect(20, 30, 141, 17))
        self.etiquetaPassAnterior.setObjectName(_fromUtf8("etiquetaPassAnterior"))
        self.etiquetaPassNueva = QtGui.QLabel(DialogoCambioPass)
        self.etiquetaPassNueva.setGeometry(QtCore.QRect(20, 70, 141, 17))
        self.etiquetaPassNueva.setObjectName(_fromUtf8("etiquetaPassNueva"))
        self.etiquetaRepetir = QtGui.QLabel(DialogoCambioPass)
        self.etiquetaRepetir.setGeometry(QtCore.QRect(20, 110, 141, 17))
        self.etiquetaRepetir.setObjectName(_fromUtf8("etiquetaRepetir"))
        self.campoPassVieja = QtGui.QLineEdit(DialogoCambioPass)
        self.campoPassVieja.setGeometry(QtCore.QRect(180, 30, 181, 27))
        self.campoPassVieja.setEchoMode(QtGui.QLineEdit.Password)
        self.campoPassVieja.setObjectName(_fromUtf8("campoPassVieja"))
        self.campoPassNueva = QtGui.QLineEdit(DialogoCambioPass)
        self.campoPassNueva.setGeometry(QtCore.QRect(180, 70, 181, 27))
        self.campoPassNueva.setEchoMode(QtGui.QLineEdit.Password)
        self.campoPassNueva.setObjectName(_fromUtf8("campoPassNueva"))
        self.campoPassRepetir = QtGui.QLineEdit(DialogoCambioPass)
        self.campoPassRepetir.setGeometry(QtCore.QRect(180, 110, 181, 27))
        self.campoPassRepetir.setEchoMode(QtGui.QLineEdit.Password)
        self.campoPassRepetir.setObjectName(_fromUtf8("campoPassRepetir"))
        self.botonAceptar = QtGui.QPushButton(DialogoCambioPass)
        self.botonAceptar.setGeometry(QtCore.QRect(430, 20, 98, 27))
        self.botonAceptar.setObjectName(_fromUtf8("botonAceptar"))
        self.botonCancelar = QtGui.QPushButton(DialogoCambioPass)
        self.botonCancelar.setGeometry(QtCore.QRect(430, 60, 98, 27))
        self.botonCancelar.setObjectName(_fromUtf8("botonCancelar"))

        self.retranslateUi(DialogoCambioPass)
        QtCore.QMetaObject.connectSlotsByName(DialogoCambioPass)

    def retranslateUi(self, DialogoCambioPass):
        DialogoCambioPass.setWindowTitle(_translate("DialogoCambioPass", "Dialog", None))
        self.etiquetaPassAnterior.setText(_translate("DialogoCambioPass", "Contraseña Anterior:", None))
        self.etiquetaPassNueva.setText(_translate("DialogoCambioPass", "Contraseña Nueva:", None))
        self.etiquetaRepetir.setText(_translate("DialogoCambioPass", "Repetir Nueva:", None))
        self.botonAceptar.setText(_translate("DialogoCambioPass", "Aceptar", None))
        self.botonCancelar.setText(_translate("DialogoCambioPass", "Cancelar", None))

