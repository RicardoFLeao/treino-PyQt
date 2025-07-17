from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt
import sys


class tela(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: blue')
        self.showMaximized()
        self.componentes()

    def componentes(self):
        label = QLabel("TITULO")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: red; font-size: 45px")

        quadro = QWidget()
        quadro.setStyleSheet("background-color: lightgray; border-radius: 10px")
        # quadro.setFixedSize(800, 500)
        quadro.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # quadro.setMinimumSize(800, 500)
        # quadro.setMaximumSize(1300, 700)


        nome = QLabel("Nome")
        editnome = QLineEdit()
        editnome.setStyleSheet("background-color: white")
        # editnome.setFixedWidth(800)

        cpf = QLabel("CPF")
        editcpf = QLineEdit()
        editcpf.setStyleSheet("background-color: white")
        editcpf.setMaximumWidth(250)
        editcpf.setMinimumWidth(200)
        editcpf.setInputMask("000.000.000-00")

        tel = QLabel("Telefone")
        edittel = QLineEdit()
        edittel.setStyleSheet("background-color: white")
        edittel.setFixedWidth(250)
        edittel.setInputMask("(00)00000-0000")

        grid = QGridLayout()
        grid.addWidget(nome, 0, 0)
        grid.addWidget(editnome, 0, 1)
        grid.addWidget(cpf, 0, 2)
        grid.addWidget(editcpf, 0, 3)
        grid.addWidget(tel, 1, 0)
        grid.addWidget(edittel, 1, 1)


        quadro.setLayout(grid)

        botao1 = QPushButton("botao 1")
        botao1.setFixedSize(120, 50)

        botao2 = QPushButton("botao 2")
        botao2.setFixedSize(120, 50)

        hbox = QHBoxLayout()
        hbox.addWidget(botao1)
        hbox.addWidget(botao2)

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(quadro)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela()
    janela.show()
    sys.exit(app.exec())