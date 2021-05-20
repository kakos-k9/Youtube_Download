from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import baixarv
import sobre_dialog
import sys


class Inicio(QDialog):
    def inicar(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(314, 450)
        Dialog.setMinimumSize(QSize(314, 450))
        Dialog.setMaximumSize(QSize(314, 450))
        Dialog.setWindowIcon(QIcon('snake.png'))
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QRect(60, 20, 191, 264))
        self.pushButton.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap("svtcobrar.jpg"))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(256, 256))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setGeometry(QRect(6, 7, 60, 16))
        font = QFont()
        font.setPointSize(7)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
        "    color: rgb(255, 255, 255);\n"
        "    background-color: rgb(212, 0, 0);\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(180, 0, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    color: rgb(0, 0, 0);\n"
        "    background-color: rgb(255, 0, 0);\n"
        "}")
        self.pushButton_2.clicked.connect(self.chama_tela_sobre)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setGeometry(QRect(60, 380, 200, 40))
        font = QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
        "    color: rgb(255, 255, 255);\n"
        "    background-color: rgb(212, 0, 0);\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(180, 0, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    color: rgb(0, 0, 0);\n"
        "    background-color: rgb(255, 0, 0);\n"
        "}")
        self.pushButton_3.clicked.connect(self.chama_tela_download)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(63, 290, 201, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(40, 330, 251, 36))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SVT COBRA R"))
        self.pushButton_2.setText(_translate("Dialog", "SOBRE [F1]"))
        self.pushButton_2.setShortcut(_translate("Dialog", "F1"))
        self.pushButton_3.setText(_translate("Dialog", "ABRIR [Enter]"))
        self.pushButton_3.setShortcut(_translate("Dialog", "Enter"))
        self.label.setText(_translate("Dialog", "SVT COBRA R"))
        self.label_2.setText(_translate("Dialog", "Clique Em Abrir ou Tecle \"Enter\""))

    def chama_tela_download(self):
        self.janela = QMainWindow()
        self.tela = baixarv.Download()
        self.tela.baixar(self.janela)
        self.janela.show()

    def chama_tela_sobre(self):
        self.janela = QDialog()
        self.tela = sobre_dialog.Ui_Dialog()
        self.tela.setupUi(self.janela)
        self.janela.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Inicio()
    ui.inicar(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
