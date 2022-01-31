import sys, time
from PySide6 import QtCore, QtGui, QtWidgets
from QRoundProgressBar import QRoundProgressBar

class Pomodoro(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pomodoro")
        self.resize(400, 400)

        self.workLabel = QtWidgets.QLabel("Work:")
        self.workLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.workTimeEdit = QtWidgets.QTimeEdit()
        self.breakLabel = QtWidgets.QLabel("Break:")
        self.breakLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.breakTimeEdit = QtWidgets.QTimeEdit()
        self.bar = QRoundProgressBar()
        self.modeLabel = QtWidgets.QLabel("WORK")
        self.modeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actionButton = QtWidgets.QPushButton("Pause")
        self.resetButton = QtWidgets.QPushButton("Reset")

        self.bar.setFixedSize(200, 200)
        self.bar.setDataPenWidth(6)
        self.bar.setOutlinePenWidth(6)
        self.bar.setFormat('00:00:00')
        # self.bar.resetFormat()
        #self.bar.setNullPosition(90)
        
        #self.bar.setDataColors([(0., QtGui.QColor.fromRgb(0, 115, 210)), (0.5, QtGui.QColor.fromRgb(0, 115, 210)), (1., QtGui.QColor.fromRgb(0, 115, 210))])

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 100, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.bar.setPalette(palette)
        self.bar.setBarStyle(QRoundProgressBar.StyleLine)

        self.bar.setRange(0, 3000)
        self.bar.setValue(50)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.workLabel, 0, 0, 1, 1)
        self.layout.addWidget(self.workTimeEdit, 0, 1, 1, 1)
        self.layout.addWidget(self.breakLabel, 0, 2, 1, 1)
        self.layout.addWidget(self.breakTimeEdit, 0, 3, 1, 1)
        self.layout.addWidget(self.bar, 1, 1, 1, 3)
        self.layout.addWidget(self.modeLabel, 2, 0, 1, 4)
        self.layout.addWidget(self.actionButton, 3, 0, 1, 2)
        self.layout.addWidget(self.resetButton, 3, 2, 1, 2)

def main():
    app = QtWidgets.QApplication(sys.argv)
    pomodoro = Pomodoro()
    pomodoro.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()