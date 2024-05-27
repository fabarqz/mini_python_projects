import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import pyperclip
import dice


class appWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # instantiate dice module
        dice_logic = dice.Dice()
        self.numbersOnly = QtGui.QIntValidator(1, 20)

        self.diceappModes = QtWidgets.QStackedLayout()

        self.diceappSimple = self.simplediceMode()

        self.diceappModes.addWidget(self.diceappSimple)

        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.addLayout(self.diceappModes)

        self.setLayout(self.mainLayout)

    def simplediceMode(self):
        widget = QtWidgets.QWidget()
        self.simplediceLayout = QtWidgets.QVBoxLayout(self)
        self.simplediceLayout.setSpacing(2)
        self.simplediceLayout.setContentsMargins(10, 10, 10, 10)

        # simple dice app layout
        self.simpleDiceLayout = QtWidgets.QVBoxLayout()
        self.simpleDiceLayoutInput = QtWidgets.QHBoxLayout()
        self.simplediceLayout.setSpacing(50)
        # simple dice app elements
        self.simpleDicePrimaryLabel = QtWidgets.QLabel("Simple Dice Roll Simulator")
        self.simpleDicePrimaryLabel.setAlignment(
            QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter
        )
        self.simpleDicePrimaryLabel.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum
        )

        self.simplediceOutput = QtWidgets.QLabel(
            "You rolled a n-sided dice. The result is"
        )
        self.simplediceOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.simplediceOutput.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum
        )

        self.simpleDiceInput = QtWidgets.QComboBox()
        self.simpleDiceInput.addItem("4")
        self.simpleDiceInput.addItem("6")
        self.simpleDiceInput.addItem("8")
        self.simpleDiceInput.addItem("10")
        self.simpleDiceInput.addItem("12")
        self.simpleDiceInput.addItem("20")
        self.simpleDiceInput.setCurrentIndex(0)
        self.simpleDiceInput.setMaximumWidth(100)

        self.simpleDiceButton = QtWidgets.QPushButton("Roll Dice")
        self.simpleDiceButton.clicked.connect(lambda: self.simplediceLogic())
        self.simpleDiceButton.setMaximumWidth(100)

        # Layout all simple dice app elements
        self.simpleDiceLayout.addWidget(self.simpleDicePrimaryLabel)
        self.simpleDiceLayout.addWidget(self.simplediceOutput)
        self.simpleDiceLayoutInput.addWidget(self.simpleDiceInput)
        self.simpleDiceLayoutInput.addWidget(self.simpleDiceButton)

        self.simplediceLayout.addLayout(self.simpleDiceLayout)
        self.simplediceLayout.addLayout(self.simpleDiceLayoutInput)

        widget.setLayout(self.simplediceLayout)
        return widget

    @QtCore.Slot()
    def simplediceLogic(self):
        diceChoice = int(self.simpleDiceInput.currentText())
        rollResult = dice.Dice().roll(diceChoice)
        self.simplediceOutput.setText(
            f"Rolled a {str(diceChoice)}-sided dice. The result is {str(rollResult)}"
        )


if __name__ == "__main__":
    dice_gui = QtWidgets.QApplication([])
    widget = appWidget()
    widget.resize(600, 400)
    widget.show()

    sys.exit(dice_gui.exec())
