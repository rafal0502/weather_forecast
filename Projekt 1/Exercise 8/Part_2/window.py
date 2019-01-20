# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.filePath_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.filePath_edit.setObjectName("filePath_edit")
        self.gridLayout.addWidget(self.filePath_edit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.quitBtt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.quitBtt.setObjectName("quitBtt")
        self.gridLayout.addWidget(self.quitBtt, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chooseFileBtt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.chooseFileBtt.setObjectName("chooseFileBtt")
        self.horizontalLayout.addWidget(self.chooseFileBtt)
        self.loadBtt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.loadBtt.setObjectName("loadBtt")
        self.horizontalLayout.addWidget(self.loadBtt)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 3)
        self.deleteBtt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.deleteBtt.setObjectName("deleteBtt")
        self.gridLayout.addWidget(self.deleteBtt, 1, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget.setMinimumSize(QtCore.QSize(781, 300))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 3, 0, 1, 3)
        self.listView = QtWidgets.QListView(self.gridLayoutWidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select file to load:"))
        self.quitBtt.setText(_translate("MainWindow", "Quit"))
        self.chooseFileBtt.setText(_translate("MainWindow", "Browse"))
        self.loadBtt.setText(_translate("MainWindow", "Load"))
        self.label_2.setText(_translate("MainWindow", "VTK Preview of selected items:"))
        self.deleteBtt.setText(_translate("MainWindow", "Delete selected"))

