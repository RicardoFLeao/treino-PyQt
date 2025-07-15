from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
import sys

class tela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Treino salvar')
        self.setFixedSize(600, 300)
        self.componentes()

    def componentes(self):
        label = QLabel("texto:")

        self.lineedit = QLineEdit()

        self.botao = QPushButton('Salvar')
        self.botao.clicked.connect(self.salvar_texto)

        self.fechar = QPushButton('Fechar')
        self.fechar.clicked.connect(self.sair)

        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(self.lineedit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.botao, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.fechar, alignment=(Qt.AlignmentFlag.AlignCenter))

        self.setLayout(vbox)

    def salvar_texto(self):
        texto = self.lineedit.text()
        with open("texto.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)

    def sair(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela()
    janela.show()
    sys.exit(app.exec())
