import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import pyperclip


class appWidget(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.userScore = 0
        self.pcScore = 0

        # initializing the widgets that will be placed in the app window

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(50, 20, 50, 50)

        # labels and the like

        self.header1 = QtWidgets.QLabel(
            "Yet another Rock, Paper, Scissors game", alignment=QtCore.Qt.AlignHCenter
        )

        self.labelsLayout = QtWidgets.QHBoxLayout()
        self.scoresLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout = QtWidgets.QHBoxLayout()

        self.horizontal_spacer = QtWidgets.QSpacerItem(
            10, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )

        self.userLabel = QtWidgets.QLabel("You")
        self.userLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.pcLabel = QtWidgets.QLabel("The guy she told you not to worry about")
        self.pcLabel.setAlignment(QtCore.Qt.AlignRight)

        self.statusLabel = QtWidgets.QLabel("Game start! Cast your fist!")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.labelsLayout.addWidget(self.userLabel)
        self.labelsLayout.addItem(self.horizontal_spacer)
        self.labelsLayout.addWidget(self.pcLabel)

        self.userScoreLabel = QtWidgets.QLabel(alignment=QtCore.Qt.AlignVCenter)
        self.userScoreLabel.setNum(self.userScore)
        self.pcScoreLabel = QtWidgets.QLabel(alignment=QtCore.Qt.AlignVCenter)
        self.pcScoreLabel.setNum(self.pcScore)

        self.scoresLayout.addWidget(self.userScoreLabel)
        self.scoresLayout.addItem(self.horizontal_spacer)
        self.scoresLayout.addWidget(self.pcScoreLabel)

        # the buttons

        self.buttonRock = QtWidgets.QPushButton("Rock")
        self.buttonPaper = QtWidgets.QPushButton("Paper")
        self.buttonScissors = QtWidgets.QPushButton("Scissors")

        self.buttonRock.clicked.connect(lambda: self.player_choice("Rock"))
        self.buttonPaper.clicked.connect(lambda: self.player_choice("Paper"))
        self.buttonScissors.clicked.connect(lambda: self.player_choice("Scissors"))

        self.buttonsLayout.addWidget(self.buttonRock)
        self.buttonsLayout.addWidget(self.buttonPaper)
        self.buttonsLayout.addWidget(self.buttonScissors)

        # laying down the widgets in the app windown

        self.layout.addWidget(self.header1)
        self.layout.addLayout(self.labelsLayout)
        self.layout.addLayout(self.scoresLayout)
        self.layout.addWidget(self.statusLabel)
        self.layout.addLayout(self.buttonsLayout)

    @QtCore.Slot()
    def player_choice(self, player_move):
        pcChoice = ["Rock", "Paper", "Scissors", "Shoot"]
        weight = [30, 30, 30, 10]
        computer_move = random.choices(pcChoice, weight)[0]

        result = self.determine_winner(player_move, computer_move)

        self.statusLabel.setText(
            f"You chose {player_move} while he chose {computer_move}. {result}"
        )

    def determine_winner(self, player, pc):
        if player == pc:
            result = "It's a draw!"
        elif (
            (player == "Rock" and pc == "Scissors")
            or (player == "Paper" and pc == "Rock")
            or (player == "Scissors" and pc == "Paper")
        ):
            self.userScore += 1
            result = "You win!"
        elif pc == "Shoot":
            # for now reset all scores to zero. figure out a proper game over scenario later
            self.userScore = 0
            self.pcScore = 0
            result = "Oh no! He's got a gun. You died"
        else:
            self.pcScore += 1
            result = "You lost!"

        # update the labels
        self.userScoreLabel.setNum(self.userScore)
        self.pcScoreLabel.setNum(self.pcScore)

        return result


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = appWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
