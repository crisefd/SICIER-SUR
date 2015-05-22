# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MTAsignarNotas.ui'
#
# Created: Fri May 22 14:57:10 2015
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

class VentanaAsignarNotas(QtGui.QFrame):
    def __init__(self):
        super(VentanaAsignarNotas, self).__init__()
        self.setupUi(self)

    def setupUi(self, VentanaAsignarNotas):
        VentanaAsignarNotas.setObjectName(_fromUtf8("VentanaAsignarNotas"))
        VentanaAsignarNotas.resize(601, 577)
        self.etiquetaTitulo_2 = QtGui.QLabel(VentanaAsignarNotas)
        self.etiquetaTitulo_2.setGeometry(QtCore.QRect(240, 0, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitulo_2.setFont(font)
        self.etiquetaTitulo_2.setObjectName(_fromUtf8("etiquetaTitulo_2"))
        self.tabWidget = QtGui.QTabWidget(VentanaAsignarNotas)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 591, 441))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.campoBusqueda = QtGui.QLineEdit(self.tab_2)
        self.campoBusqueda.setGeometry(QtCore.QRect(260, 20, 301, 29))
        self.campoBusqueda.setObjectName(_fromUtf8("campoBusqueda"))
        self.botonBuscar = QtGui.QPushButton(self.tab_2)
        self.botonBuscar.setGeometry(QtCore.QRect(240, 180, 100, 27))
        self.botonBuscar.setObjectName(_fromUtf8("botonBuscar"))
        self.comboAtributos = QtGui.QComboBox(self.tab_2)
        self.comboAtributos.setGeometry(QtCore.QRect(130, 20, 91, 25))
        self.comboAtributos.setObjectName(_fromUtf8("comboAtributos"))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.tableWidget = QtGui.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 531, 101))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.etiquetaBuscar = QtGui.QLabel(self.tab_2)
        self.etiquetaBuscar.setGeometry(QtCore.QRect(35, 20, 81, 20))
        self.etiquetaBuscar.setObjectName(_fromUtf8("etiquetaBuscar"))
        self.campoIDActualizar_3 = QtGui.QLineEdit(self.tab_2)
        self.campoIDActualizar_3.setGeometry(QtCore.QRect(260, 210, 301, 29))
        self.campoIDActualizar_3.setText(_fromUtf8(""))
        self.campoIDActualizar_3.setObjectName(_fromUtf8("campoIDActualizar_3"))
        self.etiquetaIDActualizar_2 = QtGui.QLabel(self.tab_2)
        self.etiquetaIDActualizar_2.setGeometry(QtCore.QRect(30, 220, 191, 17))
        self.etiquetaIDActualizar_2.setObjectName(_fromUtf8("etiquetaIDActualizar_2"))
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 250, 531, 101))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.botonBuscar_2 = QtGui.QPushButton(self.tab_2)
        self.botonBuscar_2.setGeometry(QtCore.QRect(240, 360, 100, 27))
        self.botonBuscar_2.setObjectName(_fromUtf8("botonBuscar_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.etiquetaIDActualizar = QtGui.QLabel(self.tab)
        self.etiquetaIDActualizar.setGeometry(QtCore.QRect(10, 40, 191, 17))
        self.etiquetaIDActualizar.setObjectName(_fromUtf8("etiquetaIDActualizar"))
        self.campoIDActualizar = QtGui.QLineEdit(self.tab)
        self.campoIDActualizar.setGeometry(QtCore.QRect(220, 30, 311, 29))
        self.campoIDActualizar.setObjectName(_fromUtf8("campoIDActualizar"))
        self.campoIDActualizar_2 = QtGui.QLineEdit(self.tab)
        self.campoIDActualizar_2.setGeometry(QtCore.QRect(220, 90, 311, 29))
        self.campoIDActualizar_2.setObjectName(_fromUtf8("campoIDActualizar_2"))
        self.etiquetaIDActualizar_3 = QtGui.QLabel(self.tab)
        self.etiquetaIDActualizar_3.setGeometry(QtCore.QRect(10, 100, 191, 17))
        self.etiquetaIDActualizar_3.setObjectName(_fromUtf8("etiquetaIDActualizar_3"))
        self.etiquetaIDActualizar_4 = QtGui.QLabel(self.tab)
        self.etiquetaIDActualizar_4.setGeometry(QtCore.QRect(10, 140, 191, 17))
        self.etiquetaIDActualizar_4.setObjectName(_fromUtf8("etiquetaIDActualizar_4"))
        self.campoIDActualizar_4 = QtGui.QLineEdit(self.tab)
        self.campoIDActualizar_4.setGeometry(QtCore.QRect(220, 140, 61, 29))
        self.campoIDActualizar_4.setObjectName(_fromUtf8("campoIDActualizar_4"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 210, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.pushButton = QtGui.QPushButton(VentanaAsignarNotas)
        self.pushButton.setGeometry(QtCore.QRect(240, 520, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(VentanaAsignarNotas)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(VentanaAsignarNotas)

    def retranslateUi(self, ventana):
        ventana.setWindowTitle(_translate("ventana", "Dialog", None))
        self.etiquetaTitulo_2.setText(_translate("ventana", "CIER-SUR", None))
        self.botonBuscar.setText(_translate("ventana", "Buscar", None))
        self.comboAtributos.setItemText(0, _translate("ventana", "Nombre", None))
        self.comboAtributos.setItemText(1, _translate("ventana", "Apellido", None))
        self.comboAtributos.setItemText(2, _translate("ventana", "ID", None))
        self.comboAtributos.setItemText(3, _translate("ventana", "Correo", None))
        self.comboAtributos.setItemText(4, _translate("ventana", "Ciudad", None))
        self.etiquetaBuscar.setText(_translate("ventana", "Buscar por:", None))
        self.etiquetaIDActualizar_2.setText(_translate("ventana", "Actualizar Notas al LT con ID", None))
        self.botonBuscar_2.setText(_translate("ventana", "Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ventana", "Buscar LT", None))
        self.tab.setToolTip(_translate("ventana", "<html><head/><body><p><br/></p></body></html>", None))
        self.etiquetaIDActualizar.setText(_translate("ventana", "Actualizar Notas al LT con ID", None))
        self.etiquetaIDActualizar_3.setText(_translate("ventana", "Actividad con ID", None))
        self.etiquetaIDActualizar_4.setText(_translate("ventana", "Nota", None))
        self.pushButton_2.setText(_translate("ventana", "Actializar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ventana", "Actualizar Notas", None))
        self.pushButton.setText(_translate("ventana", "Cancelar", None))

if __name__  == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = VentanaAsignarNotas()
    w.show()
    sys.exit(app.exec_())
