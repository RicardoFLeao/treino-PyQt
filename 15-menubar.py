from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QAction
import sys


class tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Treino menuBar")
        self.showMaximized()
        with open("estilo.css", "r") as arquivo_css:
            estilo = arquivo_css.read()
            self.setStyleSheet(estilo)

        self.componentes()

    def componentes(self):

        bmenu = QMenuBar()
        self.setMenuBar(bmenu)

        #menu arquivo
        menuArq = QMenu("Arquivo", self)
        exportar_arquivo = QMenu('Exportar', self)
        novoArq = QAction('Novo', self)
        abrirArq = QAction('Abrir', self)

        menuArq.addMenu(exportar_arquivo)
        menuArq.addSeparator()
        menuArq.addAction(novoArq)
        menuArq.addSeparator()
        menuArq.addAction(abrirArq)

        exp_arq_pdf = QAction('Exportar PDF', self)
        exp_arq_xml = QAction('Exportar XML', self)

        exportar_arquivo.addAction(exp_arq_pdf)
        exportar_arquivo.addSeparator()
        exportar_arquivo.addAction(exp_arq_xml)


        #menu cliente
        menuCli = QMenu('Cliente', self)
        novoCli = QAction('Novo cliente', self)
        relaCli = QAction('Relatórios', self)

        menuCli.addAction(novoCli)
        menuCli.addSeparator()
        menuCli.addAction(relaCli)


        #menu sair
        sair = QAction('Sair',self)
        sair.triggered.connect(self.close)

        #adiciona à barra menu
        bmenu.addMenu(menuArq)
        bmenu.addMenu(menuCli)
        bmenu.addAction(sair)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela()
    janela.show()
    sys.exit(app.exec())



