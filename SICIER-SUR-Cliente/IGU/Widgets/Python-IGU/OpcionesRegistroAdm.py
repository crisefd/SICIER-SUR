# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpcionesRegistroAdm.ui'
#
# Created: Sun May 24 18:36:05 2015
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

class VentanaOpcionesRegistroAdm(QtGui.QFrame):
    def __init__(self):
        super(VentanaOpcionesRegistroAdm, self).__init__()
        self.setupUi(self)

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
        QtCore.QMetaObject.connectSlotsByName(VentanaOpcionesRegistroAdm)

    def retranslateUi(self, VentanaOpcionesRegistroAdm):
        VentanaOpcionesRegistroAdm.setWindowTitle(_translate("VentanaOpcionesRegistroAdm", "Frame", None))
        self.label.setText(_translate("VentanaOpcionesRegistroAdm", "Registrar  Usuario", None))
        self.botonAdm.setText(_translate("VentanaOpcionesRegistroAdm", "Administrator", None))
        self.botonCoor.setText(_translate("VentanaOpcionesRegistroAdm", "Coordinator", None))

