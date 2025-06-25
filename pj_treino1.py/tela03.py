from PyQt6.QtWidgets import *
import sys


class tela3(QWidget):
    def __init__(self):
        super().__init__()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tela3()
    janela.show()
    sys.exit(app.exec())
