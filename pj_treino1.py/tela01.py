from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from tela02 import tela2
import sys


class tela1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela 1 Cadastro")
        self.setFixedSize(650, 380)
        self.componentes()

        self.produtos = []


    def componentes(self):
        lb_prod = QLabel('Produto:')

        self.ed_prod = QLineEdit()
        self.ed_prod.setPlaceholderText('Nome do produto...')

        lb_vlr = QLabel('Valor R$:')
        
        self.ed_vlr = QLineEdit()
        self.ed_vlr.setFixedWidth(80) # setFixedWidth -> fixa a largura do widget 
        
        lb_catg = QLabel('Categoria:')
        self.cb_catg = QComboBox()
        catg = ['Selecione','Alimentos', 'Bebidas', 'Limpesa', 'Perfumaria']
        self.cb_catg.addItems(catg)
        self.cb_catg.model().item(0).setEnabled(False)

        btn_add = QPushButton('Adicionar')
        btn_add.setFixedSize(150, 60)
        btn_add.clicked.connect(self.msg_add)

        self.lb_msg = QLabel()
        self.lb_msg.setFont(QFont('sanserif', 20))
        self.lb_msg2 = QLabel()

        btn_tela2 = QPushButton('Tela 2')
        btn_tela2.setFixedSize(150,60)
        btn_tela2.clicked.connect(self.prox_tela)

        hbox_pd = QHBoxLayout()
        hbox_pd.addWidget(lb_prod, alignment=Qt.AlignmentFlag.AlignLeft)
        hbox_pd.addWidget(self.ed_prod)
        hbox_pd.addWidget(lb_vlr)
        hbox_pd.addWidget(self.ed_vlr)
        hbox_pd.addWidget(lb_catg)
        hbox_pd.addWidget(self.cb_catg)

        vbox_pd = QVBoxLayout()
        vbox_pd.addLayout(hbox_pd)
        vbox_pd.addWidget(btn_add, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox_pd.addWidget(self.lb_msg, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox_pd.addWidget(self.lb_msg2, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox_pd.addWidget(btn_tela2, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox_pd.setContentsMargins(25,50,25,10)

        self.setLayout(vbox_pd)

    def msg_add(self):
        nome = self.ed_prod.text()
        valor = self.ed_vlr.text()
        categ = self.cb_catg.currentText()
        
        if nome and valor and categ != 'Selecione':
            self.lb_msg.setText('Produto adicionado!')
            self.lb_msg2.setText(f'{nome} R$ {valor},00')
            self.produtos.append((nome, valor, categ))
            self.ed_prod.clear()
            self.ed_vlr.clear()
        else:
            self.lb_msg.setText('PREENCHA TODOS OS CAMPOS!')
            self.lb_msg2.clear()

    def prox_tela(self):
        self.janela2 = tela2(self.produtos)
        self.janela2.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela1()
    janela.show()
    sys.exit(app.exec())