from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
import sys

class tela(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Lendo arquivo txt - 1')
        self.setFixedSize(600, 400)

        self.componentes()

    def componentes(self):
        label = QLabel('TEXTO')
        label.setStyleSheet("Color: red; font-size: 36px; font-style: italic;")

        self.textedit = QTextEdit()
        self.textedit.setReadOnly(True)

        botao = QPushButton('Carregar arquivo')
        botao.clicked.connect(self.leitura)


        vbox = QVBoxLayout()
        vbox.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.textedit)
        vbox.addWidget(botao, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(vbox)

    def leitura(self):
        try:
            with open("arq.txt", "r", encoding="utf-8") as texto:
                self.textedit.setPlainText(texto.read())
        except FileNotFoundError:
            self.textedit.setPlainText('Arquivo não encontrado')
                

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela()
    janela.show()
    sys.exit(app.exec())
