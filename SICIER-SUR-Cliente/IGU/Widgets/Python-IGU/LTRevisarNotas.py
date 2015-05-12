# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LTRevisarNotas.ui'
#
# Created: Tue May 12 17:08:38 2015
#      by: PyQt4 UI code generator 4.10.4
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

class VentanaRegistroLT(QtGui.QFrame):
    def __init__(self):
        super(VentanaRegistroLT, self).__init__()
        self.setupUi(self)

    def setupUi(self, ventana):
        ventana.setObjectName(_fromUtf8("ventana"))
        ventana.resize(601, 577)
        self.etiquetaTitulo_2 = QtGui.QLabel(ventana)
        self.etiquetaTitulo_2.setGeometry(QtCore.QRect(240, 0, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etiquetaTitulo_2.setFont(font)
        self.etiquetaTitulo_2.setObjectName(_fromUtf8("etiquetaTitulo_2"))
        self.tabWidget = QtGui.QTabWidget(ventana)
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
        self.comboAtributos.setGeometry(QtCore.QRect(100, 20, 151, 25))
        self.comboAtributos.setObjectName(_fromUtf8("comboAtributos"))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.comboAtributos.addItem(_fromUtf8(""))
        self.tableWidget = QtGui.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 531, 101))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.etiquetaBuscar = QtGui.QLabel(self.tab_2)
        self.etiquetaBuscar.setGeometry(QtCore.QRect(0, 20, 101, 20))
        self.etiquetaBuscar.setObjectName(_fromUtf8("etiquetaBuscar"))
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 250, 531, 101))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.botonBuscar_2 = QtGui.QPushButton(self.tab_2)
        self.botonBuscar_2.setGeometry(QtCore.QRect(190, 220, 191, 27))
        self.botonBuscar_2.setObjectName(_fromUtf8("botonBuscar_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 160, 211, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.pushButton = QtGui.QPushButton(ventana)
        self.pushButton.setGeometry(QtCore.QRect(240, 520, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(ventana)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ventana)

    def retranslateUi(self, ventana):
        ventana.setWindowTitle(_translate("ventana", "Dialog", None))
        self.etiquetaTitulo_2.setText(_translate("ventana", "CIER-SUR", None))
        self.botonBuscar.setText(_translate("ventana", "Buscar", None))
        self.comboAtributos.setItemText(0, _translate("ventana", "Nombre Actividad", None))
        self.comboAtributos.setItemText(1, _translate("ventana", "ID Actividad", None))
        self.etiquetaBuscar.setText(_translate("ventana", "Consultar por:", None))
        self.botonBuscar_2.setText(_translate("ventana", "Consultar listado completo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ventana", "Consultar notas", None))
        self.tab.setToolTip(_translate("ventana", "<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton_2.setText(_translate("ventana", "Generar certificado de notas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ventana", "Generar reportes", None))
        self.pushButton.setText(_translate("ventana", "Cerrar", None))

if __name__  == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = VentanaRegistroLT()
    w.show()
    sys.exit(app.exec_())