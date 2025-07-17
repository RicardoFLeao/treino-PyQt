from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
import sys


class tela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lendo arq para ComboBox')
        self.setFixedSize(600, 350)


        self.componentes()
    
    def componentes(self):
        label = QLabel('Selecione:')
        # label.adjustSize()
        label.setFixedSize(label.sizeHint()) # coloca a label do tamanho certo e

        self.cbox = QComboBox()

        self.cbox.currentIndexChanged.connect(self.selected)

        selecionado = QLabel('Selecionado: ')
        selecionado.setStyleSheet("margin-top: 16px;")
        selecionado.setFixedSize(selecionado.sizeHint())
        
        self.most_sel = QLabel()
        self.most_sel.setStyleSheet('color: red; font-size: 32px')

        carr = QPushButton('Carregar')
        carr.setFixedSize(110, 40)
        carr.clicked.connect(self.carr)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label)
        hbox1.addWidget(self.cbox)

        hbox2 = QHBoxLayout()

        hbox2.addWidget(selecionado)
        hbox2.addWidget(self.most_sel)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(carr, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(vbox)
        
    def carr(self):
        try:
            with open("arq.txt", "r", encoding="utf-8") as arquivo:
                self.cbox.clear()
                self.cbox.addItem('Selecione')
                self.cbox.model().item(0).setEnabled(False)
                for linha in arquivo:
                    self.cbox.addItem(linha.strip())
        except FileNotFoundError:
            self.cbox.clear()
            self.cbox.addItem("arquivo não encontrado")
    
    def selected(self):
        escolhido = self.cbox.currentText().upper()
        if escolhido != "SELECIONE":
            self.most_sel.setText(escolhido)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela()
    janela.show()
    sys.exit(app.exec())