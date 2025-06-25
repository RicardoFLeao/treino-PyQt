from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout
from PyQt6.QtCore import Qt
import sys

class tela3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TELA NÚMERO 3")
        self.setFixedSize(700, 450)
        self.componentes()

    def componentes(self):
        self.ant = QPushButton('Tela 2')
        self.ant.setFixedSize(150, 60)
        self.ant.clicked.connect(self.abrir_tela2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.ant, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)

    def abrir_tela2(self):
        from tela2 import tela2
        self.janela2 = tela2()
        self.janela2.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela3()
    janela.show()
    sys.exit(app.exec())
