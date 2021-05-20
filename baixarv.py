from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pytube import YouTube
import ajuda_dialog
import sys



class Download(QMainWindow):
    def baixar(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setWindowIcon(QIcon('play.png'))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(95, 30, 625, 41))
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(340, 120, 151, 111))
        self.pushButton.setStyleSheet("border: 2px solid rgb(0, 0, 0);")
        self.pushButton.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap("play.png"))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(128, 128))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QRect(130, 250, 81, 22))
        self.comboBox.setStyleSheet("QComboBox {\n"
        "       color: rgb(255, 255, 255);\n"
        "       background-color: rgb(20, 20, 20);\n"
        "       border-radius: 5px;\n"
        "}\n"
        "")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(140, 300, 41, 31))
        font = QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QRect(140, 340, 551, 31))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "QLineEdit:focus {\n"
        "    border: 2px solid rgb(0, 85, 255);\n"
        "}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QRect(140, 420, 171, 31))
        font = QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QRect(140, 460, 561, 31))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "QLineEdit:focus {\n"
        "    border: 2px solid rgb(0, 85, 255);\n"
        "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(190, 520, 411, 51))
        font = QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
        "       color: rgb(255, 255, 255);\n"
        "       background-color: rgb(212, 0, 0);\n"
        "       border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "      background-color: rgb(180, 0, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "       color: rgb(0, 0, 0);\n"
        "        background-color: rgb(255, 0, 0);\n"
        "}")
        self.pushButton_2.clicked.connect(self.download)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QRect(6, 7, 60, 16))
        font = QFont()
        font.setPointSize(7)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
        "       color: rgb(255, 255, 255);\n"
        "       background-color: rgb(212, 0, 0);\n"
        "       border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "      background-color: rgb(180, 0, 0);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "       color: rgb(0, 0, 0);\n"
        "        background-color: rgb(255, 0, 0);\n"
        "}")
        self.pushButton_3.clicked.connect(self.chama_tela_ajuda)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Baixar Músicas/Vídeos do Youtube"))
        self.label.setText(_translate("MainWindow", "Baixar Músicas/Vídeos do Youtube"))
        self.label_2.setText(_translate("MainWindow", "Link"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Insira o Link do Vídeo Que Deseja Baixar"))
        self.label_3.setText(_translate("MainWindow", "Local de Download"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Insira o Local Que Será Armazenado o Video Por Exmplo: C:\\\\Users\\\\Usuario\\\\Desktop\\\\Pasta "))
        self.pushButton_2.setText(_translate("MainWindow", "DOWNLOAD [Enter]"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Enter"))
        self.pushButton_3.setText(_translate("MainWindow", "AJUDA [F1]"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "F1"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MP3"))
        self.comboBox.setItemText(1, _translate("MainWindow", "MP4"))

    def download(self):
        if self.comboBox.currentText() == "MP3":

            self.link = self.lineEdit.text()
            self.local = self.lineEdit_2.text()

            try:
                self.yt = YouTube(self.link)
                self.ys = self.yt.streams.get_audio_only()

                QMessageBox.information(QMessageBox(), 'kaiqueafonsoferreira21@gmail.com', f'Título: {self.yt.title}\nNúmero de views: {self.yt.views}\nTamanho do Vídeo: {self.yt.length} Segundos\nAvaliação do Vídeo: {self.yt.rating}')
                QMessageBox.information(QMessageBox(), 'kaiqueafonsoferreira21@gmail.com', 'Baixando...')
                self.ys.download(self.local)
                QMessageBox.information(QMessageBox(), 'kaiqueafonsoferreira21@gmail.com', 'Download Completo! Verfique Sua Pasta Que Você Destinou')

                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
            except Exception as ERROR:
                print(ERROR)
                QMessageBox.warning(QMessageBox(), 'ERROR', 'VERIFQUE SE O LINK E O LOCAL DE DOWNLOAD ESTÃO CORRETOS!')
        else:

            self.link = self.lineEdit.text()
            self.local = self.lineEdit_2.text()

            try:
                self.yt = YouTube(self.link)
                self.ys = self.yt.streams.get_highest_resolution()

                QMessageBox.information(QMessageBox(), 'kaiqueafonsoferreira21@gmail.com',
                                        f'Título: {self.yt.title}\nNúmero de views: {self.yt.views}\nTamanho do Vídeo: {self.yt.length} Segundos\nAvaliação do Vídeo: {self.yt.rating}')
                QMessageBox.information(QMessageBox(), 'kaiqueafonsoferreira21@gmail.com', 'Baixando...')
                self.ys.download(self.local)
                QMessageBox.information(QMessageBox(), 'kaiqueafonsoferreira21@gmail.com',
                                        'Download Completo! Verfique Sua Pasta Que Você Destinou')

                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
            except Exception as ERROR:
                print(ERROR)
                QMessageBox.warning(QMessageBox(), 'ERROR', 'VERIFQUE SE O LINK E O LOCAL DE DOWNLOAD ESTÃO CORRETOS!')

    def chama_tela_ajuda(self):
        self.janela = QDialog()
        self.tela = ajuda_dialog.Ajuda()
        self.tela.help(self.janela)
        self.janela.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Download()
    ui.baixar(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
