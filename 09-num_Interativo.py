from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QTimer
import sys

class tela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Números interativos')
        self.setFixedSize(450,350)
        self.cor_atual = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.piscar)


        self.componentes()

    def componentes(self):

        label_1 = QLabel('Valor:')
        self.label_2 = QLabel('0')

        self.btn_1 = QPushButton('Adiciona + 1')
        self.btn_1.setFixedSize(110, 40)
        self.btn_1.clicked.connect(self.adicionar)

        btn_2 = QPushButton('Zerar')
        btn_2.setFixedSize(110, 40)
        btn_2.clicked.connect(self.zerar)

        btn_3 = QPushButton('Subtrair - 1')
        btn_3.setFixedSize(110, 40)
        btn_3.clicked.connect(self.subtrair)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(self.label_2)

        hbox_btn = QHBoxLayout()
        hbox_btn.addWidget(self.btn_1)
        hbox_btn.addWidget(btn_3)

        vbox_btn = QVBoxLayout()
        vbox_btn.addLayout(hbox_btn)
        vbox_btn.addWidget(btn_2, alignment=Qt.AlignmentFlag.AlignCenter)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox1)
        vbox1.addLayout(vbox_btn)

        self.setLayout(vbox1)


    def atualiza_cor(self, num):
        if num % 10 == 0 and num != 0: # se for multiplo de 10 liga o metodo timer
            self.timer.start(400) # inicia o metodo timer com o tempo de 200 milesegundos
        else:
            self.timer.stop() # desliga o metodo timer <- assim ele permanece desligado
            if num % 5 == 0 and num != 0: # se for multiplo de 5 muda as cores 
                self.label_2.setStyleSheet("color: red; font-size: 20px")
            else:
                self.label_2.setStyleSheet("color: black")

    def piscar(self): # metodo para mudar as cores 
        if self.cor_atual: # vincula a cor_atual false a red
            self.label_2.setStyleSheet("color: blue; font-size: 20px")
        else: # vincula a cor_atual true a black
            self.label_2.setStyleSheet("color: green; font-size: 20px")
        self.cor_atual = not self.cor_atual # ve qual boleano esta e inverte 

    def adicionar(self):
        num = int(self.label_2.text())
        num += 1
        self.label_2.setText(str(num))
        self.atualiza_cor(num)


    def subtrair(self):
        num = int(self.label_2.text())
        if num > 0:
            num -= 1
            self.label_2.setText(str(num))
            self.atualiza_cor(num)


    def zerar(self):
        self.label_2.setText('0')
        self.label_2.setStyleSheet("color: black")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela()
    janela.show()
    sys.exit(app.exec())