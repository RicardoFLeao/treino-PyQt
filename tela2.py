from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

import sys

class tela2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TELA NÚMERO 2')
        self.setFixedSize(700, 450)
        self.componentes()

    def componentes(self):
        prox = QPushButton('Tela 3')
        prox.setFixedSize(150, 60)
        prox.clicked.connect(self.abrir_tela3)

        ant = QPushButton('Tela 1')
        ant.setFixedSize(150, 60)
        ant.clicked.connect(self.abrir_tela1)

        hbox = QHBoxLayout()
        hbox.addWidget(ant, alignment=Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(prox, alignment=Qt.AlignmentFlag.AlignRight)
        hbox.setContentsMargins(95, 0, 95, 0)

        self.setLayout(hbox)

    def abrir_tela1(self):
        from tela1 import tela1
        self.janela1 = tela1()
        self.janela1.show()
        self.close()

    def abrir_tela3(self):
        from tela3 import tela3
        self.janela3 = tela3()
        self.janela3.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela2()
    janela.show()
    sys.exit(app.exec())
