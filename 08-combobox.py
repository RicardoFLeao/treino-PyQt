from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
import sys

class tela(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.setWindowTitle("Treinando com combo box")
        self.componentes()


    def componentes(self):
        item = QLabel('Item:')
        # item.setContentsMargins(10,0,0,0)

        self.item_edit = QLineEdit()


        self.lista_itens = QComboBox()
        self.lista_itens.addItem('Selecione')
        self.lista_itens.model().item(0).setEnabled(False)
        self.lista_itens.currentIndexChanged.connect(self.selec_item)

        self.item_selec = QLabel('Item selecionado:')

        
        bt_add = QPushButton('Adicionar')
        bt_add.setFixedSize(150,70)
        bt_add.clicked.connect(self.adicionar)

        
        hbox_item = QHBoxLayout()
        hbox_item.addWidget(item)
        hbox_item.addWidget(self.item_edit)
        hbox_item.setContentsMargins(10,0,0,0)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_item)
        vbox.addWidget(self.lista_itens)
        vbox.addWidget(self.item_selec)
        vbox.addWidget(bt_add, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.setContentsMargins(20, 70, 20, 10)
        self.setLayout(vbox)


    def adicionar(self):
        item = self.item_edit.text()
        self.lista_itens.addItem(item)
        self.item_edit.clear() # <- tem outra forma de limpar ou fiz do jeito certo

    def selec_item(self):
        escolhido = self.lista_itens.currentText()
        self.item_selec.setText(f'Item selecionado: {escolhido}')

app = QApplication(sys.argv)
janela = tela()
janela.show()
sys.exit(app.exec())