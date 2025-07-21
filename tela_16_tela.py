from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QAction, QIcon
import sys


class tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("imagens/icone.png"))
        self.setWindowTitle("treino tela")
        with open('estilo.css', 'r') as estilo_css:
            estilo = estilo_css.read()        
            self.setStyleSheet(estilo)

        self.menu()
        self.componentes()
        self.showMaximized()
        
    def menu(self):

        #menu
        bmenu = QMenuBar()
        self.setMenuBar(bmenu)

        arquivo = QMenu('Arquivo', self)

        salvar = QAction('Salvar', self)



        sair = QAction('Sair', self)
        sair.triggered.connect(self.close)

        arquivo.addAction(salvar)
        arquivo.addAction(sair)

        utilitarios = QMenu('Utilitarios', self)
        uti_export = QMenu('Exportar', self)
        uti_export_pdf = QAction('Exportar PDF', self)
        uti_export_xml = QAction('Exportar XML', self)

        utilitarios.addMenu(uti_export)
        uti_export.addAction(uti_export_pdf)
        uti_export.addAction(uti_export_xml)

        bmenu.addMenu(arquivo)
        bmenu.addMenu(utilitarios)

    def componentes(self):
                #botões
        central = QWidget()

        btn_prox = QPushButton('Proxima Tela')
        btn_prox.clicked.connect(self.abri_tela2)

        btn_prox.setFixedSize(250, 80)

        hbox = QHBoxLayout(central)
        hbox.addWidget(btn_prox)

        self.setCentralWidget(central)

    def abri_tela2(self):
        from tela_16_tela2 import tela2
        self.nova_tela = tela2()
        self.nova_tela.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela()
    janela.show()
    sys.exit(app.exec())