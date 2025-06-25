from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys


class tela(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 500)
        self.componentes()


    def componentes(self):

        btn1 = QPushButton('botao da esquerda')
        btn1.setFixedSize(250, 80)
        btn2 = QPushButton('botao da direita')
        btn2.setFixedSize(250, 80)

        label = QLabel('Label ao centro')

        hbox = QHBoxLayout()
        hbox.addWidget(btn1, alignment=Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(btn2, alignment=Qt.AlignmentFlag.AlignRight)

        vbox = QVBoxLayout()
        vbox.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


app = QApplication(sys.argv)
janela = tela()
janela.show()
sys.exit(app.exec())