from PyQt6.QtWidgets import *
import sys


class tela(QWidget):
    def __init__(self):
        super().__init__()
        self.componentes()

    def componentes(self):

        btn1 = QPushButton('botão 1')
        btn2 = QPushButton('botão 2')
        btn3 = QPushButton('botão 3')

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        self.setLayout(hbox)
   

app = QApplication(sys.argv)
janela = tela()
janela.show()
sys.exit(app.exec())