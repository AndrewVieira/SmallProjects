import sys
from PySide6 import QtCore, QtGui, QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)

    wid = QtWidgets.QWidget()
    wid.resize(800, 600)
    wid.move(300, 300)

    editLabel = QtWidgets.QLabel("Enter Text to Convert Here")
    textEdit = QtWidgets.QPlainTextEdit()
    convertButton = QtWidgets.QPushButton("Convert Text")
    resultLabel = QtWidgets.QLabel("Result")

    wid.layout = QtWidgets.QVBoxLayout(wid)
    wid.layout.addWidget(editLabel)
    wid.layout.addWidget(textEdit)
    wid.layout.addWidget(convertButton)
    wid.layout.addWidget(resultLabel)

    wid.setWindowTitle('Pig Latin Converter')
    wid.show()

    sys.exit(app.exec())

def to_pig_latin(string):
    result = ""

    words = string.split()

    for word in words:
        pass

if __name__ == '__main__':
    main()