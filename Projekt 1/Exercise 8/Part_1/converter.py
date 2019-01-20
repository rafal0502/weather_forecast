# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ex8_v2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import QIcon, QPixmap, QImage, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtCore import QFile
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_ImageConverter(QtWidgets.QMainWindow):
    def setupUi(self, ImageConverter):
        ImageConverter.setObjectName("ImageConverter")
        ImageConverter.resize(639, 531)
        self.centralwidget = QtWidgets.QWidget(ImageConverter)
        self.centralwidget.setObjectName("centralwidget")
        self.RedWeight = QtWidgets.QLabel(self.centralwidget)
        self.RedWeight.setGeometry(QtCore.QRect(20, 110, 81, 41))
        self.RedWeight.setObjectName("RedWeight")
        self.BlueWeight = QtWidgets.QLabel(self.centralwidget)
        self.BlueWeight.setGeometry(QtCore.QRect(160, 110, 91, 41))
        self.BlueWeight.setObjectName("BlueWeight")
        self.GreenWeight = QtWidgets.QLabel(self.centralwidget)
        self.GreenWeight.setGeometry(QtCore.QRect(300, 110, 101, 41))
        self.GreenWeight.setObjectName("GreenWeight")
        self.Convert = QtWidgets.QPushButton(self.centralwidget)
        self.Convert.setGeometry(QtCore.QRect(480, 120, 97, 27))
        self.Convert.setObjectName("Convert")
        self.SaveAs = QtWidgets.QPushButton(self.centralwidget)
        self.SaveAs.setGeometry(QtCore.QRect(20, 420, 97, 27))
        self.SaveAs.setObjectName("SaveAs")
        self.Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Quit.setGeometry(QtCore.QRect(130, 420, 97, 27))
        self.Quit.setObjectName("Quit")
        self.red = QtWidgets.QLineEdit(self.centralwidget)
        self.red.setGeometry(QtCore.QRect(100, 120, 41, 21))
        self.red.setObjectName("red")
        self.blue = QtWidgets.QLineEdit(self.centralwidget)
        self.blue.setGeometry(QtCore.QRect(250, 120, 41, 21))
        self.blue.setObjectName("blue")
        self.green = QtWidgets.QLineEdit(self.centralwidget)
        self.green.setGeometry(QtCore.QRect(400, 120, 41, 21))
        self.green.setObjectName("green")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 201, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 161, 21))
        self.label_2.setObjectName("label_2")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(110, 170, 391, 211))
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.Select_file = QtWidgets.QPushButton(self.centralwidget)
        self.Select_file.setGeometry(QtCore.QRect(480, 30, 97, 27))
        self.Select_file.setObjectName("Select_file")
        self.file_text = QtWidgets.QLineEdit(self.centralwidget)
        self.file_text.setGeometry(QtCore.QRect(150, 30, 251, 21))
        self.file_text.setObjectName("file_text")
        ImageConverter.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ImageConverter)
        self.statusbar.setObjectName("statusbar")
        ImageConverter.setStatusBar(self.statusbar)
        self.actionChoose_file = QtWidgets.QAction(ImageConverter)
        self.actionChoose_file.setObjectName("actionChoose_file")
        self.actionOpen = QtWidgets.QAction(ImageConverter)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(ImageConverter)
        self.Quit.clicked.connect(ImageConverter.close)
        QtCore.QMetaObject.connectSlotsByName(ImageConverter)
        self.connect_to_actions()

        self.ImageObject = QImage()
        self.pixmap = QPixmap()
        self.converted_pixmap = QPixmap()

        self.red.setText("11")
        self.green.setText("16")
        self.blue.setText("5")




    def retranslateUi(self, ImageConverter):
        _translate = QtCore.QCoreApplication.translate
        ImageConverter.setWindowTitle(_translate("ImageConverter", "MainWindow"))
        self.RedWeight.setText(_translate("ImageConverter", "Red weight:"))
        self.BlueWeight.setText(_translate("ImageConverter", "Blue weight:"))
        self.GreenWeight.setText(_translate("ImageConverter", "Green weight: "))
        self.Convert.setText(_translate("ImageConverter", "Convert"))
        self.SaveAs.setText(_translate("ImageConverter", "Save As"))
        self.Quit.setText(_translate("ImageConverter", "Quit"))
        self.label.setText(_translate("ImageConverter", "Convert to grayscale"))
        self.label_2.setText(_translate("ImageConverter", "Select file to show"))
        self.Select_file.setText(_translate("ImageConverter", "Select"))
        self.actionChoose_file.setText(_translate("ImageConverter", "Choose file"))
        self.actionOpen.setText(_translate("ImageConverter", "Open"))
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(110, 170, 391, 211))
        self.Image.setText("")
        self.Image.setObjectName("Image")






    def connect_to_actions(self):
        self.Quit.clicked.connect(self.close_application)
        self.Select_file.clicked.connect(self.load_image)
        self.Convert.clicked.connect(self.convert_image)
        self.SaveAs.clicked.connect(self.save_image)


    def load_image(self):
        fileName = QFileDialog.getOpenFileName()
        pixmap = QPixmap()
        pixmap.load(fileName[0])
        self.Image.setPixmap(pixmap)




    def save_image(self):
        save_file = QFileDialog.getSaveFileName(self, 'Save file', '', 'JPEG file (*.jpg, *png)')
        print(save_file)
        file = QFile(save_file[0])
        self.converted_pixmap.save(file, "PNG")



    def convert_image(self):
        temporary: QImage = self.pixmap.toImage()

        red_weight = int(self.red.text())
        blue_weight = int(self.blue.text())
        green_weight = int(self.green.text())

        sum_weight = red_weight + blue_weight + green_weight

        for y in range(0, temporary.height()):
            for x in range(0, temporary.width()):
                color: QColor = temporary.pixelColor(x, y)
                red = color.red()
                green = color.green()
                blue = color.blue()
                gray = (red * red_weight + green * green_weight + blue * blue_weight) / sum_weight
                new_color = QColor()
                new_color.setRgb(gray, gray, gray)
                temporary.setPixelColor(x, y, new_color)


        self.converted_pixmap = QPixmap.fromImage(temporary)
        self.Image.setPixmap(self.converted_pixmap)



    def close_application(self):
        sys.exit()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageConverter = QtWidgets.QMainWindow()
    ui = Ui_ImageConverter()
    ui.setupUi(ImageConverter)
    ImageConverter.show()
    sys.exit(app.exec_())

