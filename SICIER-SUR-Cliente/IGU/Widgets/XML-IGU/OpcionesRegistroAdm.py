# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpcionesRegistroAdm.ui'
#
# Created: Thu May  7 09:42:16 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!
import sys

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

class VentanaRegistroUsuario(QtGui.QFrame):
    def setupUi(self, VentanaRegistroUsuario):
        VentanaRegistroUsuario.setObjectName(_fromUtf8("VentanaRegistroUsuario"))
        VentanaRegistroUsuario.resize(332, 308)
        VentanaRegistroUsuario.setFrameShape(QtGui.QFrame.StyledPanel)
        VentanaRegistroUsuario.setFrameShadow(QtGui.QFrame.Raised)
        self.groupBox = QtGui.QGroupBox(VentanaRegistroUsuario)
        self.groupBox.setGeometry(QtCore.QRect(50, 50, 231, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radbtnAdm = QtGui.QRadioButton(self.groupBox)
        self.radbtnAdm.setGeometry(QtCore.QRect(10, 30, 141, 22))
        self.radbtnAdm.setObjectName(_fromUtf8("radbtnAdm"))
        self.radbtnCoor = QtGui.QRadioButton(self.groupBox)
        self.radbtnCoor.setGeometry(QtCore.QRect(10, 60, 116, 22))
        self.radbtnCoor.setObjectName(_fromUtf8("radbtnCoor"))
        self.radbtnMT = QtGui.QRadioButton(self.groupBox)
        self.radbtnMT.setGeometry(QtCore.QRect(10, 90, 131, 22))
        self.radbtnMT.setObjectName(_fromUtf8("radbtnMT"))
        self.radbtnLT = QtGui.QRadioButton(self.groupBox)
        self.radbtnLT.setGeometry(QtCore.QRect(10, 120, 141, 22))
        self.radbtnLT.setObjectName(_fromUtf8("radbtnLT"))
        self.botonSig = QtGui.QPushButton(VentanaRegistroUsuario)
        self.botonSig.setGeometry(QtCore.QRect(180, 250, 98, 27))
        self.botonSig.setObjectName(_fromUtf8("botonSig"))
        self.botonAtras = QtGui.QPushButton(VentanaRegistroUsuario)
        self.botonAtras.setGeometry(QtCore.QRect(40, 250, 98, 27))
        self.botonAtras.setObjectName(_fromUtf8("botonAtras"))

        self.retranslateUi(VentanaRegistroUsuario)
        QtCore.QMetaObject.connectSlotsByName(VentanaRegistroUsuario)
    def __init__(self):
    	super(VentanaRegistroUsuario, self).__init__()
    	self.setupUi(self)

    def retranslateUi(self, VentanaRegistroUsuario):
        VentanaRegistroUsuario.setWindowTitle(_translate("VentanaRegistroUsuario", "Frame", None))
        self.groupBox.setTitle(_translate("VentanaRegistroUsuario", "Registrar Usuario", None))
        self.radbtnAdm.setText(_translate("VentanaRegistroUsuario", "Administrator", None))
        self.radbtnCoor.setText(_translate("VentanaRegistroUsuario", "Coordinator", None))
        self.radbtnMT.setText(_translate("VentanaRegistroUsuario", "Master Teacher", None))
        self.radbtnLT.setText(_translate("VentanaRegistroUsuario", "Leader Teacher", None))
        self.botonSig.setText(_translate("VentanaRegistroUsuario", "Siguiente", None))
        self.botonAtras.setText(_translate("VentanaRegistroUsuario", "Atras", None))

if __name__  == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = VentanaRegistroUsuario()
    w.show()
    sys.exit(app.exec_())
