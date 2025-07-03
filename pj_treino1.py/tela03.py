from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
import sys


class tela3(QWidget):
    def __init__(self, produtos):
        super().__init__()
        self.produtos = produtos
        self.setWindowTitle('Tela 3 consulta')
        self.setFixedSize(650, 380)
        self.componentes()


    def componentes(self):
        btn_tela2 = QPushButton("Tela 2")
        btn_tela2.setFixedSize(150, 60)
        btn_tela2.clicked.connect(self.voltar_tl2)

        vbox = QVBoxLayout()
        vbox.addWidget(btn_tela2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)

    def voltar_tl2(self):
        from tela02 import tela2
        self.janela2 = tela2(self.produtos)
        self.janela2.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela3()
    janela.show()
    sys.exit(app.exec())
