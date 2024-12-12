# 12/4/24 Last change is to add text box in Ezgamba that acceots bet.
# 12/5/24 Added button to ezgamba layout and some more comments
# 12/6/24 created test fucntion fo buttonbet to change text of results label
# 12/9/24 working on betlogic

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

    # mini-game
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
        self.ezgambaCash.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.ezgambaCash.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum
        )

        # label where results are displayed

        self.gambaResults = QtWidgets.QLabel(" Insert Text here ")
        self.gambaResults.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.gambaResults.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum
        )

        # Input area for bet. Configured to only accept integers)

        self.inputBet = QtWidgets.QLineEdit()
        self.inputBet.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.inputBet.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum
        )
        self.inputBet.setText(str(self.currentBet))
        # responsible for limiting the input bet to numbers from 1 to 9999
        self.inputBet.setValidator(intOnly)
        # bet buttons
        self.betHeads = QtWidgets.QPushButton("Heads")
        self.betHeads.clicked.connect(lambda: self.betlogic_heads())
        self.betHeads.setMaximumWidth(500)
        self.betHeads.move(50, 100)
        self.betTails = QtWidgets.QPushButton("Tails")
        self.betTails.clicked.connect(lambda: self.betlogic_tails())
        self.betTails.setMaximumWidth(500)
        self.betTails.move(200, 100)

        self.resetGame = QtWidgets.QPushButton("Reset")
        self.resetGame.hide()

        # appending of widgets to main layout

        self.ezgambaLayout.addWidget(ezgambatitle)
        self.ezgambaLayout.addWidget(self.gambaResults)
        self.ezgambaLayout.addWidget(self.ezgambaCash)
        self.ezgambaLayout.addWidget(self.inputBet)

        self.ezgambaLayout.addWidget(self.betHeads)
        self.ezgambaLayout.addWidget(self.betTails)
        self.ezgambaLayout.addWidget(self.resetGame)

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

    def betlogic_tails(self):

        # check if player can still bet:
        self.currentBet = int(self.inputBet.text())
        if self.availableCash < 0 or self.availableCash < self.currentBet:
            if self.availableCash == 0 or self.availableCash < 0:
                self.gambaResults.setText("You have 0 remaining cash. Game Over!")
            elif self.availableCash < self.currentBet:
                self.gambaResults.setText(
                    "Your cannot make a bet higher than your remaining cash. Lower the amount then try again."
                )
        else:
            self.tossResult = self.coin_logic.singleToss()

            if self.tossResult == "Heads":
                self.gambaResults.setText(f"The result is {self.tossResult}. You lost!")
                self.availableCash = self.availableCash - int(self.currentBet)
            else:
                self.gambaResults.setText(f"The result is Tails. You won!")
                self.availableCash = self.availableCash + int(self.currentBet)
            self.ezgambaCash.setText(str(self.availableCash))

    def betlogic_heads(self):
        # check if player can still bet:
        self.currentBet = int(self.inputBet.text())
        if self.availableCash < 0 or self.availableCash < self.currentBet:
            if self.availableCash == 0 or self.availableCash < 0:
                self.gambaResults.setText("You have 0 remaining cash. Game Over!")
            elif self.availableCash < self.currentBet:
                self.gambaResults.setText(
                    "Your cannot make a bet higher than your remaining cash. Lower the amount then try again."
                )
        else:
            self.tossResult = self.coin_logic.singleToss()

            if self.tossResult == "Tails":
                self.gambaResults.setText(f"The result is {self.tossResult}. You lost!")
                self.availableCash = self.availableCash - int(self.currentBet)
            else:
                self.gambaResults.setText(f"The result is Heads. You won!")
                self.availableCash = self.availableCash + int(self.currentBet)
            self.ezgambaCash.setText(str(self.availableCash))

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
