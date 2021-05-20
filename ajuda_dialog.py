from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys



class Ajuda(QDialog):
    def help(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 300)
        Dialog.setWindowIcon(QIcon('snake.png'))
        Dialog.setMinimumSize(QSize(450, 300))
        Dialog.setMaximumSize(QSize(450, 300))
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(190, 10, 61, 31))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(20, 70, 411, 151))
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ajuda"))
        self.label.setText(_translate("Dialog", "Ajuda"))
        self.label_2.setText(_translate("Dialog", "Ao Copiar o Link do Vídeo do Youtube, Cole no Primeiro Campo\n"
        "Depois Clique Com o Botão Direito na Pasta Que Você Deseja\n"
        "Salvar o Arquivo Clique em Propriedades e Copie o Que Está\n"
        "escrito em \"Local\" Logo Após Cole no Campo de Download\n"
        "Adicione uma Contra Barra a Mais em Todas Elas no Campo\n"
        "e Coloque o Nome da Pasta e Já Pode Efetuar o Download.\n"
        "Logo a Cima do Campo \"link\" Selecione o Formato do Arquivo\n"
        "MP3(Aúdio) ou MP4(Vídeo)."))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ajuda()
    ui.help(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
