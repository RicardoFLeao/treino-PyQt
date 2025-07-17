from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QAction, QFont
import sys


class tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('imagens/icone.png'))
        self.setWindowTitle('Sistema de altomação')
        self.setStyleSheet('background-color: #01050D;')
        self.menu()
        self.componentes()
        self.showMaximized()

    def menu(self):
        bmenu = self.menuBar()

        bmenu.addMenu("Cadastro")
        bmenu.addMenu("Produto")
        bmenu.addMenu("Utilitários")

        sair = QAction("Sair", self)
        sair.triggered.connect(self.close)
        bmenu.addAction(sair)

        bmenu.setStyleSheet('color: white')
        # bmenu.setFont(QFont("sanserif"))

    def componentes(self):
        central= QWidget()

        vbox = QVBoxLayout(central)
        nitro = QLabel("Nitro Sys")
        nitro.setStyleSheet("font-size: 78px; color: white")

        gbotoes = QGridLayout()

        botao1 = QPushButton("botão 1")
        botao2 = QPushButton("botão 2")
        botao3 = QPushButton("botão 3")
        botao4 = QPushButton("botão 4")
        botao5 = QPushButton("botão 5")
        botao6 = QPushButton("botão 6")

        botoes = [botao1 , botao2, botao3, botao4, botao5, botao6]

        for botao in botoes:
            botao.setFixedSize(340,80)
            botao.setStyleSheet("background-color: #031740; color: white")
        
        gbotoes.addWidget(botao1, 0,0)
        gbotoes.addWidget(botao2, 0,1)
        gbotoes.addWidget(botao3, 1,0)
        gbotoes.addWidget(botao4, 1,1)
        gbotoes.addWidget(botao5, 2,0)
        gbotoes.addWidget(botao6, 2,1)

        hbox=QHBoxLayout()

        notas = QTextEdit()
        notas.setFixedSize(400, 350)
        notas.setStyleSheet("background-color: white; color: black; border-radius: 10px")

        hbox.addLayout(gbotoes)
        hbox.addWidget(notas)

        vbox.addWidget(nitro, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addLayout(hbox)


        self.setCentralWidget(central)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela()
    janela.show()
    sys.exit(app.exec())
