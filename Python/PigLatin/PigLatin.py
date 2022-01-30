import sys
from PySide6 import QtCore, QtGui, QtWidgets

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
punctuation = ['.', ',', '!', '?', '\'']
endpunctuation = ['.', '?', '!']

class PigLatinConverter:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

        self.widget = QtWidgets.QWidget()
        self.widget.resize(800, 600)
        self.widget.move(300, 300)

        self.editLabel = QtWidgets.QLabel("Enter Text to Convert Here")
        self.textEdit = QtWidgets.QPlainTextEdit()
        self.convertButton = QtWidgets.QPushButton("Convert Text")
        self.convertButton.clicked.connect(self.toPigLatin)
        self.resultText = QtWidgets.QPlainTextEdit("Result will show here")
        self.resultText.setEnabled(False)

        self.widget.layout = QtWidgets.QGridLayout(self.widget)
        self.widget.layout.setSpacing(10)

        self.widget.layout.addWidget(self.editLabel, 1, 0, 1, 1)
        self.widget.layout.addWidget(self.textEdit, 2, 0, 1, 5)
        self.widget.layout.addWidget(self.convertButton, 3, 0, 1, 1)
        self.widget.layout.addWidget(self.resultText, 4, 0, 1, 5)

        self.widget.setWindowTitle('Pig Latin Converter')
        self.widget.show()

        sys.exit(self.app.exec())

    def toPigLatin(self):
        text = self.textEdit.toPlainText()
        result = ""

        words = text.split()

        wordsLen = len(words)
        capitalize = True

        for word in words:            
            newWord = word
            punc = ""

            while newWord[-1] in punctuation:
                punc = newWord[-1] + punc
                newWord = newWord[0:-1]
            
            if newWord == newWord.capitalize():
                capitalize = True

            if len(newWord) < 2:
                pass
            elif not (newWord[0] in vowels) and (newWord[1] in vowels) and not (newWord[1] in punctuation):
                newWord = newWord[1:] + newWord[0] + "ay"
            else:
                newWord = newWord + "yay"
            
            newWord = newWord.lower()
            if capitalize == True:
                newWord = newWord[0].upper() + newWord[1:]
                capitalize = False

            result += newWord
            result += punc

            if newWord[-1] in endpunctuation:
                capitalize = True
            
            if words.index(word) != wordsLen:
                result += " "
            
        self.resultText.setPlainText(result)
        self.resultText.setEnabled(True)

if __name__ == '__main__':
    app = PigLatinConverter()