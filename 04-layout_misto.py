from PyQt6.QtWidgets import *
import sys

class tela (QWidget):
    def __init__(self):
        super().__init__()
        self.componentes()

    def componentes(self):
        btn1 = QPushButton('botao 1')
        btn2 = QPushButton('botao 2')
        btn3 = QPushButton('botao 3')

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        label = QLabel('TITULO')

        vbox = QVBoxLayout()

        vbox.addWidget(label)
        vbox.addLayout(hbox)

        vbox.setSpacing(20)
        vbox.setContentsMargins(100, 100, 100, 100)
        self.setLayout(vbox)

app = QApplication(sys.argv)
janela = tela()
janela.show()
sys.exit(app.exec())