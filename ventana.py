# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VenPrincipal(object):
    def setupUi(self, VenPrincipal):
        VenPrincipal.setObjectName("VenPrincipal")
        VenPrincipal.resize(712, 481)
        self.centralwidget = QtWidgets.QWidget(VenPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.lblDNI = QtWidgets.QLabel(self.centralwidget)
        self.lblDNI.setGeometry(QtCore.QRect(30, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblDNI.setFont(font)
        self.lblDNI.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDNI.setObjectName("lblDNI")
        self.centralwidget_2 = QtWidgets.QPushButton(self.centralwidget)
        self.centralwidget_2.setGeometry(QtCore.QRect(380, 240, 75, 23))
        self.centralwidget_2.setObjectName("centralwidget_2")
        self.lblxes = QtWidgets.QLabel(self.centralwidget)
        self.lblxes.setGeometry(QtCore.QRect(300, 20, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblxes.setFont(font)
        self.lblxes.setAutoFillBackground(False)
        self.lblxes.setStyleSheet("\n"
"font: 11pt \"Calibri\";\n"
"background-color: rgb(15, 111, 255);")
        self.lblxes.setObjectName("lblxes")
        self.lblapel = QtWidgets.QLabel(self.centralwidget)
        self.lblapel.setGeometry(QtCore.QRect(20, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblapel.setFont(font)
        self.lblapel.setAlignment(QtCore.Qt.AlignCenter)
        self.lblapel.setObjectName("lblapel")
        self.centralwidget_3 = QtWidgets.QPushButton(self.centralwidget)
        self.centralwidget_3.setGeometry(QtCore.QRect(480, 240, 75, 23))
        self.centralwidget_3.setObjectName("centralwidget_3")
        self.lblnome = QtWidgets.QLabel(self.centralwidget)
        self.lblnome.setGeometry(QtCore.QRect(380, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblnome.setFont(font)
        self.lblnome.setAlignment(QtCore.Qt.AlignCenter)
        self.lblnome.setObjectName("lblnome")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(100, 55, 511, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(90, 200, 511, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 100, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 140, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(460, 130, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        VenPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VenPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        VenPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VenPrincipal)
        self.statusbar.setObjectName("statusbar")
        VenPrincipal.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(VenPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(VenPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VenPrincipal)

    def retranslateUi(self, VenPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VenPrincipal.setWindowTitle(_translate("VenPrincipal", "MainWindow"))
        self.lblDNI.setText(_translate("VenPrincipal", "DNI"))
        self.centralwidget_2.setText(_translate("VenPrincipal", "Aceptar"))
        self.lblxes.setText(_translate("VenPrincipal", "Xestión Clientes"))
        self.lblapel.setText(_translate("VenPrincipal", "APELLIDOS"))
        self.centralwidget_3.setText(_translate("VenPrincipal", "Salir"))
        self.lblnome.setText(_translate("VenPrincipal", "NOMBRE"))
        self.menuArchivo.setTitle(_translate("VenPrincipal", "Archivo"))
        self.actionSalir.setText(_translate("VenPrincipal", "Salir"))
