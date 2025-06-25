from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys


class tela(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 500)
        self.componentes()

    def componentes(self):
        lb1 = QLabel('Exercício de Fixação')
        lb1.setFixedSize(400, 50)
        lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lb1.setStyleSheet("""
                            background-color: blue;
                            color: red;
                          """)
        lb1.setFont(QFont('sanserif', 25))
        lb2 = QLabel('Escolha uma das opções:')
        lb2.setFixedSize(400, 50)
        lb2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lb2.setStyleSheet("""
                            background-color: green;
                            color: white;
                          """)
        lb2.setFont(QFont('sanserif', 25))
        btn1 = QPushButton('Opção A')
        btn1.setFixedSize(150, 40)
        btn2 = QPushButton('Opção B')
        btn2.setFixedSize(150, 40)
        btn3 = QPushButton('Opção C')
        btn3.setFixedSize(150, 40)

        vbox = QVBoxLayout()
        vbox.addWidget(lb1, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(lb2, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(btn1, alignment=Qt.AlignmentFlag.AlignLeft)
        vbox.addWidget(btn2, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(btn3, alignment=Qt.AlignmentFlag.AlignRight)


        vbox.setContentsMargins(50, 50, 50, 50)
        vbox.setSpacing(15)


        self.setLayout(vbox)


app = QApplication(sys.argv)
janela = tela()
janela.show()
sys.exit(app.exec())

