# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(406, 330)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.depth_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.depth_lineEdit.setGeometry(QtCore.QRect(190, 25, 191, 22))
        self.depth_lineEdit.setObjectName("depth_lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.load_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_btn.setGeometry(QtCore.QRect(90, 260, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.load_btn.setFont(font)
        self.load_btn.setObjectName("load_btn")
        self.file_path_btn = QtWidgets.QPushButton(self.centralwidget)
        self.file_path_btn.setGeometry(QtCore.QRect(190, 101, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.file_path_btn.setFont(font)
        self.file_path_btn.setObjectName("file_path_btn")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Создание теплокарты"))
        self.label.setText(_translate("MainWindow", "Выберите глубину:"))
        self.label_2.setText(_translate("MainWindow", "Выберите файл:"))
        self.load_btn.setText(_translate("MainWindow", "Загрузить теплокарту"))
        self.file_path_btn.setText(_translate("MainWindow", "Выбрать файл"))

