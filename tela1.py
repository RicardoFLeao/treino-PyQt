from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from tela2 import tela2
import sys


class tela1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TELA NÚMERO 1')
        self.setFixedSize(700, 450)
        self.componentes()


    def componentes(self):
        prox = QPushButton('TELA 2')
        prox.setFixedSize(150, 60)
        prox.clicked.connect(self.abrir_tela2)

        vbox = QVBoxLayout()
        vbox.addWidget(prox, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)
    
    def abrir_tela2(self):
        self.janela2 = tela2()
        self.janela2.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela1()
    janela.show()
    sys.exit(app.exec())



