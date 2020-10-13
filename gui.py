##########
# IMPORT #
##########
from sys import argv
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit,\
        QTextBrowser
from controllers.controller import Controller

__author__ = "rick@gnous.eu"
__licence__ = "GPL3"

class Interface(QMainWindow):
    def __init__(self):
        super(Interface, self).__init__()

        self.setWindowTitle("Parser Juniper")
        self.ui = uic.loadUi("views/principal.ui")
        self.setCentralWidget(self.ui)

        inputText = self.ui.findChildren(QTextEdit, "inputText")[0]
        outputText = self.ui.findChildren(QTextBrowser, "outputText")[0]
        parseButton = self.ui.findChildren(QPushButton, "parse")[0]
        quitButton = self.ui.findChildren(QPushButton, "quit")[0]

        self.controller = Controller(inputText, outputText)

        parseButton.clicked.connect(self.controller.click)
        quitButton.clicked.connect(quit)

        self.show()

if __name__ == "__main__":
    app = QApplication(argv)
    window = Interface()
    exit(app.exec_())
