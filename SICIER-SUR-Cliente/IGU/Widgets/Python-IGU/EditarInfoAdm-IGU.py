# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditarInfoAdm-IGU.ui'
#
# Created: Fri May  8 10:22:13 2015
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

class VentanaEditarInfoAdm(QtGui.QFrame):

    def __init__(self):
        super(VentanaEditarInfoAdm, self).__init__()
        self.dialogoCambioPass = DialogoCambioPass()
        self.setupUi(self)

    def setupUi(self, VentanaEditarInfoAdm):
        VentanaEditarInfoAdm.setObjectName(_fromUtf8("VentanaEditarInfoAdm"))
        VentanaEditarInfoAdm.resize(530, 293)
        self.etiquetaTel = QtGui.QLabel(VentanaEditarInfoAdm)
        self.etiquetaTel.setGeometry(QtCore.QRect(60, 50, 66, 17))
        self.etiquetaTel.setObjectName(_fromUtf8("etiquetaTel"))
        self.etiquetaDir = QtGui.QLabel(VentanaEditarInfoAdm)
        self.etiquetaDir.setGeometry(QtCore.QRect(60, 100, 66, 17))
        self.etiquetaDir.setObjectName(_fromUtf8("etiquetaDir"))
        self.etiquetaCiudad = QtGui.QLabel(VentanaEditarInfoAdm)
        self.etiquetaCiudad.setGeometry(QtCore.QRect(60, 150, 66, 17))
        self.etiquetaCiudad.setObjectName(_fromUtf8("etiquetaCiudad"))
        self.campoTel = QtGui.QLineEdit(VentanaEditarInfoAdm)
        self.campoTel.setGeometry(QtCore.QRect(150, 50, 161, 27))
        self.campoTel.setObjectName(_fromUtf8("campoTel"))
        self.campoDir = QtGui.QLineEdit(VentanaEditarInfoAdm)
        self.campoDir.setGeometry(QtCore.QRect(150, 100, 161, 27))
        self.campoDir.setObjectName(_fromUtf8("campoDir"))
        self.campoCiudad = QtGui.QLineEdit(VentanaEditarInfoAdm)
        self.campoCiudad.setGeometry(QtCore.QRect(150, 150, 161, 27))
        self.campoCiudad.setObjectName(_fromUtf8("campoCiudad"))
        self.botonCambPass = QtGui.QPushButton(VentanaEditarInfoAdm)
        self.botonCambPass.setGeometry(QtCore.QRect(350, 50, 151, 27))
        self.botonCambPass.setObjectName(_fromUtf8("botonCambPass"))
        self.botonActualizar = QtGui.QPushButton(VentanaEditarInfoAdm)
        self.botonActualizar.setGeometry(QtCore.QRect(190, 230, 111, 31))
        self.botonActualizar.setObjectName(_fromUtf8("botonActualizar"))

        self.retranslateUi(VentanaEditarInfoAdm)
        QtCore.QObject.connect(self.botonCambPass, QtCore.SIGNAL(_fromUtf8("pressed()")), VentanaEditarInfoAdm.mostrarDialogoPass)
        QtCore.QMetaObject.connectSlotsByName(VentanaEditarInfoAdm)

    def retranslateUi(self, VentanaEditarInfoAdm):
        VentanaEditarInfoAdm.setWindowTitle(_translate("VentanaEditarInfoAdm", "Editar Info", None))
        self.etiquetaTel.setText(_translate("VentanaEditarInfoAdm", "Teléfono:", None))
        self.etiquetaDir.setText(_translate("VentanaEditarInfoAdm", "Dirección:", None))
        self.etiquetaCiudad.setText(_translate("VentanaEditarInfoAdm", "Ciudad:", None))
        self.botonCambPass.setText(_translate("VentanaEditarInfoAdm", "Cambiar Contraseña", None))
        self.botonActualizar.setText(_translate("VentanaEditarInfoAdm", "Actualizar Info.", None))

    def mostrarDialogoPass(self):
        self.dialogoCambioPass.show()

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

if __name__  == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = VentanaEditarInfoAdm()
    w.show()
    sys.exit(app.exec_())