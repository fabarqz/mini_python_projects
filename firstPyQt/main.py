import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import pyperclip


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = [
            "Hallo Welt",
            "Hei maailma",
            "Hola Mundo",
            "Witaj świecie",
            "Kaixo Mundua",
            "Hej Verden",
            "Kumusta Mundo",
        ]
        self.button = QtWidgets.QPushButton("Do not click!")
        self.copyButton = QtWidgets.QPushButton("Do not Copy")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.copyButton)
        self.button.clicked.connect(self.magic)
        self.copyButton.clicked.connect(self.copy)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

    def copy(self):
        copied_text = self.text.text()
        pyperclip.copy(copied_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
