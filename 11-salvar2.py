from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
import sys

class tela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Treino salvar arquivo - 2")
        self.setFixedSize(600, 300)
        self.componentes()

    def componentes(self):
        label = QLabel('texto')

        self.lineedit = QLineEdit()

        salvar = QPushButton('Salvar')
        salvar.clicked.connect(self.salvar)


        fechar = QPushButton('Fechar')
        fechar.clicked.connect(self.sair)

        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(self.lineedit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(salvar, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(fechar, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(vbox)

    def salvar(self):
        texto = self.lineedit.text()
        with open("arq.txt", "a", encoding="utf-8") as f:
            f.write(texto + "\n")
        self.lineedit.clear()
        self.lineedit.setFocus()

    def sair(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela()
    janela.show()
    sys.exit(app.exec())
