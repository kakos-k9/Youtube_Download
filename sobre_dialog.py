from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        Dialog.setWindowIcon(QIcon("snake.png"))
        Dialog.resize(450, 300)
        Dialog.setMinimumSize(QSize(450, 300))
        Dialog.setMaximumSize(QSize(450, 300))
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(190, 10, 61, 31))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(10, 50, 275, 31))
        font = QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QRect(10, 270, 275, 31))
        font = QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setGeometry(QRect(10, 120, 400, 61))
        font = QFont()
        font.setPointSize(8)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sobre"))
        self.label.setText(_translate("Dialog", "SOBRE"))
        self.label_2.setText(_translate("Dialog", "SVT COBRA R V1.0 Copyright © 2021 Kaique Afonso\n"
        "Todos os Direitos Reservados."))
        self.label_3.setText(_translate("Dialog", "kaiqueafonsoferreira21@gmail.com"))
        self.label_4.setText(_translate("Dialog", "\"Pois é preciso que gritemos tão alto a verdade, que demos tal relevo à verdade\n"
        "que os surdos a ouçam e os próprios cegos a vejam\""))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
