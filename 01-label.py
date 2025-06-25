from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
import sys


class tela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('01-treino PyQt6')
        self.setWindowIcon(QIcon('imagens/icone.png'))
        self.resize(500, 450)

        self.label = QLabel(self)
        self.label.setText('Ricardo Ferreira')
        self.label.setStyleSheet("""background-color: red; color: black
                                         """)
        self.label.move(155, 100)

        self.botao = QPushButton(self)
        self.botao.setText('clique aqui')
        self.botao.move(100, 130)
        self.botao.resize(150, 50)
        self.botao.clicked.connect(self.mudar_texto)

        self.botao_voltar = QPushButton(self)
        self.botao_voltar.setText('Voltar')
        self.botao_voltar.move(300, 130)
        self.botao_voltar.resize(150, 50)
        self.botao_voltar.clicked.connect(self.volta_texto)

    def mudar_texto(self):
        self.label.setText('o botão clicado muda para faze grande')
        self.label.adjustSize()

    def volta_texto(self):
        self.label.setText('Ricardo Ferreira')
        self.label.adjustSize()

app = QApplication(sys.argv)
janela = tela()
janela.show()
sys.exit(app.exec())