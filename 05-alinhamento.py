from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys


class tela(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 500)
        self.componentes()

    def componentes(self):

        label = QLabel('texto fica no centro')
        btn1 = QPushButton('botao direita')
        btn1.setFixedSize(250, 80)
        btn2 = QPushButton('botao esquerda')
        btn2.setFixedSize(250, 80)
        
        vbox = QVBoxLayout()
        vbox.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(btn1, alignment=Qt.AlignmentFlag.AlignRight)
        vbox.addWidget(btn2, alignment=Qt.AlignmentFlag.AlignLeft)
        self.setLayout(vbox)

app = QApplication(sys.argv)
janela = tela()
janela.show()
sys.exit(app.exec())
