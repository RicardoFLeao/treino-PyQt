from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QComboBox, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys


class tela2(QWidget):
    def __init__(self, produtos):
        super().__init__()
        self.produtos = produtos
        self.setWindowTitle('Tela 2 consulta')
        self.setFixedSize(650, 380)

        self.componentes()

    def componentes(self):
        lb_select = QLabel('Selecione:')
        # lb_select.adjustSize()
        lb_select.setFixedWidth(70)

        self.cb_select = QComboBox()
        self.cb_select.currentIndexChanged.connect(self.selecionado)

        self.lb_selecionado = QLabel()
        self.lb_selecionado.setFont(QFont('sanserif', 20))


        self.btn_tela1 = QPushButton('Tela 1')
        self.btn_tela1.setFixedSize(150, 60)
        self.btn_tela1.clicked.connect(self.tela_ant)

        self.btn_tela3 = QPushButton('Tela 3')
        self.btn_tela3.setFixedSize(150, 60)
        self.btn_tela3.clicked.connect(self.prox_tela)

        hbox_selc = QHBoxLayout()
        hbox_selc.addWidget(lb_select)
        hbox_selc.addWidget(self.cb_select)

        hbox_btn = QHBoxLayout()
        hbox_btn.addWidget(self.btn_tela1)
        hbox_btn.addWidget(self.btn_tela3)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_selc)
        vbox.addWidget(self.lb_selecionado, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addLayout(hbox_btn)
        vbox.setContentsMargins(20, 50, 20, 50)

        for nome, valor, categoria in self.produtos:
            self.cb_select.addItem(f"{nome} - R$ {valor} ({categoria})")

        self.setLayout(vbox)

    def selecionado(self):
        msg = self.cb_select.currentText()
        self.lb_selecionado.setText(msg)


    def tela_ant(self):
        from tela01 import tela1
        self.janela1 = tela1()
        self.janela1.show()
        self.close()

    def prox_tela(self):
        from tela03 import tela3
        self.janela3 = tela3(self.produtos)
        self.janela3.show()
        self.close()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela2()
    janela.show()
    sys.exit(app.exec())

    