# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpcionesRegistroCoor.ui'
#
# Created: Sun May 24 20:18:26 2015
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

class VentanaRegistroUsuario(QtGui.QFrame):
    def __init__(self):
        super(VentanaRegistroUsuario, self).__init__()
        self.setupUi(self)

    def setupUi(self, VentanaRegistroUsuario):
        VentanaRegistroUsuario.setObjectName(_fromUtf8("VentanaRegistroUsuario"))
        VentanaRegistroUsuario.resize(297, 217)
        VentanaRegistroUsuario.setFrameShape(QtGui.QFrame.StyledPanel)
        VentanaRegistroUsuario.setFrameShadow(QtGui.QFrame.Raised)
        self.label = QtGui.QLabel(VentanaRegistroUsuario)
        self.label.setGeometry(QtCore.QRect(40, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.botonMT = QtGui.QPushButton(VentanaRegistroUsuario)
        self.botonMT.setGeometry(QtCore.QRect(90, 80, 100, 27))
        self.botonMT.setObjectName(_fromUtf8("botonMT"))
        self.botonCoor = QtGui.QPushButton(VentanaRegistroUsuario)
        self.botonCoor.setGeometry(QtCore.QRect(90, 150, 100, 27))
        self.botonCoor.setObjectName(_fromUtf8("botonCoor"))

        self.retranslateUi(VentanaRegistroUsuario)
        QtCore.QMetaObject.connectSlotsByName(VentanaRegistroUsuario)

    def retranslateUi(self, VentanaRegistroUsuario):
        VentanaRegistroUsuario.setWindowTitle(_translate("VentanaRegistroUsuario", "Frame", None))
        self.label.setText(_translate("VentanaRegistroUsuario", "Registrar  Usuario", None))
        self.botonMT.setText(_translate("VentanaRegistroUsuario", "MasterTeacher", None))
        self.botonCoor.setText(_translate("VentanaRegistroUsuario", "Coordinator", None))

