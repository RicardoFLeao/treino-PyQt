from PyQt6.QtWidgets import *
import sys


class tela(QWidget):
    def __init__(self):
        super().__init__()
        self.componentes()
    

    def componentes(self):
        self.label = QLabel('LABEL')
        self.btn1 = QPushButton(self)
        self.btn1.setText('botão 1')
        self.btn2 = QPushButton(self)
        self.btn2.setText('botão 2')

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        self.setLayout(vbox)


app = QApplication(sys.argv)
janela = tela()
janela.show()
sys.exit(app.exec())

