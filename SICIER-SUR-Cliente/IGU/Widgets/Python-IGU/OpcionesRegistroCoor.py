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

class VentanaOpcionesRegistroCoor(QtGui.QFrame):
    def __init__(self):
        super(VentanaOpcionesRegistroCoor, self).__init__()
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

    def retranslateUi(self, VentanaOpcionesRegistroCoor):
        VentanaOpcionesRegistroCoor.setWindowTitle(_translate("VentanaOpcionesRegistroCoor", "Frame", None))
        self.label.setText(_translate("VentanaOpcionesRegistroCoor", "Registrar  Usuario", None))
        self.botonMT.setText(_translate("VentanaOpcionesRegistroCoor", "MasterTeacher", None))
        self.botonCoor.setText(_translate("VentanaOpcionesRegistroCoor", "Coordinator", None))

