# Last change is to add text box in Ezgamba that acceots bet.


import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import pyperclip
import dice
import coin


class appWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # instantiate dice module
        self.dice_logic = dice.Dice()
        self.coin_logic = coin.Coin()
        # Setting up the different application modes
        self.diceappModes = QtWidgets.QStackedLayout()

        self.diceappMenu = self.menuBox()

        self.diceappSimple = self.simplediceMode()
        self.diceappCoin = self.cointossMode()
        self.diceappGamba = self.ezgambaMode()

        self.diceappModes.addWidget(self.diceappSimple)
        self.diceappModes.addWidget(self.diceappCoin)
        self.diceappModes.addWidget(self.diceappGamba)
        self.mainLayout = QtWidgets.QHBoxLayout(self)
        self.mainLayout.addWidget(self.diceappMenu)
        self.mainLayout.addLayout(self.diceappModes)

        self.setLayout(self.mainLayout)

    def menuBox(self):
        menuWidget = QtWidgets.QWidget()
        self.menubuttonholderLayout = QtWidgets.QVBoxLayout(self)
        self.menubuttonholderLayout.setSpacing(2)
        self.menubuttonholderLayout.setContentsMargins(20, 20, 20, 20)

        self.cointossButton = QtWidgets.QPushButton("Coin Toss")
        self.simpledicemodeButton = QtWidgets.QPushButton("Simple Dice")
        self.ezgambamodeButton = QtWidgets.QPushButton("EZ Gamba Game")

        self.cointossButton.clicked.connect(self.showcointToss)
        self.simpledicemodeButton.clicked.connect(self.showsimpleDice)
        self.ezgambamodeButton.clicked.connect(self.showezGamba)

        self.menubuttonholderLayout.addWidget(self.cointossButton)
        self.menubuttonholderLayout.addWidget(self.simpledicemodeButton)
        self.menubuttonholderLayout.addWidget(self.ezgambamodeButton)
        menuWidget.setLayout(self.menubuttonholderLayout)
        return menuWidget

    def cointossMode(self):
        cointossWidget = QtWidgets.QWidget()
        self.cointossLayout = QtWidgets.QVBoxLayout(self)
        self.cointossLayout.setSpacing(0)
        self.cointossLayout.setContentsMargins(20, 20, 20, 20)

        self.cointossLabel = QtWidgets.QLabel("Coin Toss Simulator")
        self.cointossLabel.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.cointossLabel.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum
        )

        self.cointossOutput = QtWidgets.QLabel("Toss a coin")
        self.cointossOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.cointossOutput.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum
        )

        self.simplecointossButton = QtWidgets.QPushButton("Toss")
        self.simplecointossButton.clicked.connect(lambda: self.cointossLogic())
        self.simplecointossButton.setMaximumWidth(100)

        self.cointossLayout.addWidget(self.cointossLabel)
        self.cointossLayout.addWidget(self.cointossOutput)
        self.cointossLayout.addWidget(
            self.simplecointossButton, alignment=QtCore.Qt.AlignHCenter
        )

        cointossWidget.setLayout(self.cointossLayout)
        return cointossWidget

    def simplediceMode(self):
        simplediceWidget = QtWidgets.QWidget()
        self.simplediceLayout = QtWidgets.QVBoxLayout(self)
        self.simplediceLayout.setSpacing(100)
        self.simplediceLayout.setContentsMargins(20, 20, 20, 20)

        # simple dice app layout
        self.simpleDiceLayout = QtWidgets.QVBoxLayout()
        self.simpledicelayoutInput = QtWidgets.QHBoxLayout()
        self.simplediceLayout.setSpacing(100)
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
        self.simpledicelayoutInput.addWidget(self.simpleDiceInput)
        self.simpledicelayoutInput.addWidget(self.simpleDiceButton)

        self.simplediceLayout.addLayout(self.simpleDiceLayout)
        self.simplediceLayout.addLayout(self.simpledicelayoutInput)

        simplediceWidget.setLayout(self.simplediceLayout)
        return simplediceWidget

    def ezgambaMode(self):
        # EZ Gamba variables
        self.availableCash = 10000
        self.currentBet = 0
        intOnly = QtGui.QIntValidator(1, 9999)

        ezgambaWidget = QtWidgets.QWidget()
        self.ezgambaLayout = QtWidgets.QVBoxLayout(self)

        ezgambatitle = QtWidgets.QLabel("EZ Gamba Game")
        ezgambatitle.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        ezgambatitle.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum
        )
        self.ezgambaCash = QtWidgets.QLabel(str(self.availableCash))
        self.ezgambaLayout.addWidget(ezgambatitle)
        self.ezgambaLayout.addWidget(self.ezgambaCash)

        self.inputBet = QtWidgets.QLineEdit()
        self.inputBet.setValidator(intOnly)
        self.ezgambaLayout.addWidget(self.inputBet)

        ezgambaWidget.setLayout(self.ezgambaLayout)
        return ezgambaWidget

    @QtCore.Slot()
    def simplediceLogic(self):
        diceChoice = int(self.simpleDiceInput.currentText())
        rollResult = self.dice_logic.roll(diceChoice)
        self.simplediceOutput.setText(
            f"Rolled a {str(diceChoice)}-sided dice. The result is {str(rollResult)}"
        )

    def cointossLogic(self):
        result = self.coin_logic.singleToss()
        self.cointossOutput.setText(f"You toss a coin. It landed on {result}")

    def betLogic(self):
        return

    def showsimpleDice(self):
        self.diceappModes.setCurrentIndex(0)

    def showcointToss(self):
        self.diceappModes.setCurrentIndex(1)

    def showezGamba(self):
        self.diceappModes.setCurrentIndex(2)


if __name__ == "__main__":
    dice_gui = QtWidgets.QApplication([])
    widget = appWidget()
    widget.resize(600, 400)
    widget.show()

    sys.exit(dice_gui.exec())
