# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaAgregarCohortesui.ui'
#
# Created: Sat May 23 21:47:44 2015
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

class VentanaAgregarCohorte(QtGui.QFrame):
    def __init__(self):
        super(VentanaAgregarCohorte, self).__init__()
        self.setupUi(self)

    def setupUi(self, VentanaAgregarCohorte):
    	VentanaAgregarCohorte.setObjectName(_fromUtf8("VentanaAgregarCohorte"))
        VentanaAgregarCohorte.resize(421, 229)
        VentanaAgregarCohorte.setFrameShape(QtGui.QFrame.StyledPanel)
        VentanaAgregarCohorte.setFrameShadow(QtGui.QFrame.Raised)
        self.etiquetaTitulo = QtGui.QLabel(VentanaAgregarCohorte)
        self.etiquetaTitulo.setGeometry(QtCore.QRect(90, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitulo.setFont(font)
        self.etiquetaTitulo.setObjectName(_fromUtf8("etiquetaTitulo"))
        self.formLayoutWidget = QtGui.QWidget(VentanaAgregarCohorte)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 80, 291, 51))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.etiquetaCohorteID = QtGui.QLabel(self.formLayoutWidget)
        self.etiquetaCohorteID.setObjectName(_fromUtf8("etiquetaCohorteID"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.etiquetaCohorteID)
        self.campoCohorteID = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCohorteID.setObjectName(_fromUtf8("campoCohorteID"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.campoCohorteID)
        self.botonAgregar = QtGui.QPushButton(VentanaAgregarCohorte)
        self.botonAgregar.setGeometry(QtCore.QRect(130, 160, 141, 27))
        self.botonAgregar.setObjectName(_fromUtf8("botonAgregar"))

        self.retranslateUi(VentanaAgregarCohorte)
        QtCore.QMetaObject.connectSlotsByName(VentanaAgregarCohorte)

    def retranslateUi(self, VentanaAgregarCohorte):
        VentanaAgregarCohorte.setWindowTitle(_translate("VentanaAgregarCohorte", "Frame", None))
        self.etiquetaTitulo.setText(_translate("VentanaAgregarCohorte", "Agregar Cohortes", None))
        self.etiquetaCohorteID.setText(_translate("VentanaAgregarCohorte", "Cohorte ID:", None))
        self.botonAgregar.setText(_translate("VentanaAgregarCohorte", "Agregar a curso", None))

if __name__  == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = VentanaAgregarCohorte()
    w.show()
    sys.exit(app.exec_())