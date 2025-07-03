from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox
from PyQt6.QtCore import Qt
import sys

class tela4(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #67E4EB')
        self.setWindowTitle('Tela 4 - Cadastro .')
        self.setFixedSize(650, 400)
        self.componentes()

    def componentes(self):
        lb_nome = QLabel('Nome:')
        self.ed_nome = QLineEdit()

        lb_idade = QLabel('Idade:')
        self.ed_idade = QLineEdit()
        self.ed_idade.setFixedWidth(50)

        lb_sexo = QLabel('Sexo:')
        self.cb_sexo = QComboBox()
        self.cb_sexo.addItem(' ')
        self.cb_sexo.addItem('M')
        self.cb_sexo.addItem('F')
        self.cb_sexo.model().item(0).setEnabled(False)

        bt_cad = QPushButton('Cadastrar')
        bt_cad.setFixedSize(150,60)
        bt_cad.clicked.connect(self.salvar)

        self.lb_cad = QLabel()

        hbox = QHBoxLayout()
        hbox.addWidget(lb_nome)
        hbox.addWidget(self.ed_nome)
        hbox.addWidget(lb_idade)
        hbox.addWidget(self.ed_idade)
        hbox.addWidget(lb_sexo)
        hbox.addWidget(self.cb_sexo)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(bt_cad, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.lb_cad, alignment=Qt.AlignmentFlag.AlignRight)
        vbox.setContentsMargins(25,50,25,10)
        self.setLayout(vbox)

    def salvar(self):
        nome = self.ed_nome.text().strip().upper()
        idade = self.ed_idade.text().strip()
        sexo = self.cb_sexo.currentText()

        if nome and idade and sexo != " ":
            with open('cadastro.txt', 'a', encoding='utf-8') as cad:
                cad.write(f'{nome};{idade};{sexo}\n')
            self.lb_cad.setText('Cadastro Salvo!')
            self.ed_nome.clear()
            self.ed_nome.setFocus()
            self.ed_idade.clear()

        else:
            self.lb_cad.setText('Dados Invalidos!!!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela4()
    janela.show()
    sys.exit(app.exec())