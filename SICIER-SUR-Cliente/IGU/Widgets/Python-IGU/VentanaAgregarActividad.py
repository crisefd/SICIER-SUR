# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaAgregarActividad.ui'
#
# Created: Sun May 24 16:41:46 2015
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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(435, 337)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.etiquetaTitulo = QtGui.QLabel(Frame)
        self.etiquetaTitulo.setGeometry(QtCore.QRect(110, 30, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitulo.setFont(font)
        self.etiquetaTitulo.setObjectName(_fromUtf8("etiquetaTitulo"))
        self.formLayoutWidget = QtGui.QWidget(Frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 90, 311, 181))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.etiquetaIDActividad = QtGui.QLabel(self.formLayoutWidget)
        self.etiquetaIDActividad.setObjectName(_fromUtf8("etiquetaIDActividad"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.etiquetaIDActividad)
        self.etiquetaFechaInicio = QtGui.QLabel(self.formLayoutWidget)
        self.etiquetaFechaInicio.setObjectName(_fromUtf8("etiquetaFechaInicio"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.etiquetaFechaInicio)
        self.etiquetaFechaFin = QtGui.QLabel(self.formLayoutWidget)
        self.etiquetaFechaFin.setObjectName(_fromUtf8("etiquetaFechaFin"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.etiquetaFechaFin)
        self.selectorFechaInicio = QtGui.QDateEdit(self.formLayoutWidget)
        self.selectorFechaInicio.setObjectName(_fromUtf8("selectorFechaInicio"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.selectorFechaInicio)
        self.campoIDActividad = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoIDActividad.setObjectName(_fromUtf8("campoIDActividad"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.campoIDActividad)
        self.selectorFechaFin = QtGui.QDateEdit(self.formLayoutWidget)
        self.selectorFechaFin.setObjectName(_fromUtf8("selectorFechaFin"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.selectorFechaFin)
        self.etiquetaPeso = QtGui.QLabel(self.formLayoutWidget)
        self.etiquetaPeso.setObjectName(_fromUtf8("etiquetaPeso"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.etiquetaPeso)
        self.campoPeso = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoPeso.setObjectName(_fromUtf8("campoPeso"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.campoPeso)
        self.botonAgregar = QtGui.QPushButton(Frame)
        self.botonAgregar.setGeometry(QtCore.QRect(150, 280, 131, 27))
        self.botonAgregar.setObjectName(_fromUtf8("botonAgregar"))

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.etiquetaTitulo.setText(_translate("Frame", "Agregar Actividades", None))
        self.etiquetaIDActividad.setText(_translate("Frame", "ID actividad", None))
        self.etiquetaFechaInicio.setText(_translate("Frame", "Fecha Inicio", None))
        self.etiquetaFechaFin.setText(_translate("Frame", "Fecha Fin", None))
        self.etiquetaPeso.setText(_translate("Frame", "Peso:", None))
        self.botonAgregar.setText(_translate("Frame", "Agregar a curso", None))

