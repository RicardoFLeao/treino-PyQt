from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys



class tela2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela 2 ")

        with open("estilo.css", "r") as modelo_css:
            estilo = modelo_css.read()
            self.setStyleSheet(estilo)

        self.componentes()
        self.showMaximized()



    def componentes(self):
        
        btn_ant = QPushButton("Tela Anterior")
        btn_ant.clicked.connect(self.abre_tela1)

        btn_prox = QPushButton("Proxima tela")

        btn_sair = QPushButton('Sair')
        btn_sair.clicked.connect(self.sair)

        botoes = [btn_ant, btn_prox, btn_sair]

        for botao in botoes:
            botao.setFixedSize(250, 80)

        hbox = QHBoxLayout()
        hbox.setSpacing(10)
        hbox.addWidget(btn_ant)
        hbox.addWidget(btn_prox)
        

        vbox = QVBoxLayout()
        vbox.setContentsMargins(310, 280, 310, 280)
        vbox.addLayout(hbox)
        vbox.addWidget(btn_sair, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(vbox)

    def sair(self):
        self.close()

    def abre_tela1 (self):
        from tela_16_tela import tela
        self.janela1 = tela()
        self.janela1.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela2()
    janela.show()
    sys.exit(app.exec())