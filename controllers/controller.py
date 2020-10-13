##########
# IMPORT #
##########
from PyQt5.QtWidgets import QTextEdit, QTextBrowser
from parser import ParserJuniper

__author__ = "rick@gnous.eu"
__licence__ = "GPL3"

class Controller:
    def __init__(self, inputText, outputText):
        """
        Init the controller

        :param inputText QTextEdit: the area where Juniper conf in write
        :param outputText QTextBrowser: area where a series of set 
                                        command is showed
        """
        self.inputText = inputText
        self.outputText = outputText
        self.parser = ParserJuniper()

    def click(self):
        """
        Called when the user press the Parse button. 
        Gets the text of inputText and parse it. Shows the result on
        outputText.
        """
        self.parser.resetTree()
        textToParse = self.inputText.toPlainText()
        parsedText = ""
        for line in textToParse.splitlines():
            textConf = self.parser.parse(line)
            if textConf:
                parsedText += textConf + "\n"
        self.outputText.setText(parsedText)
