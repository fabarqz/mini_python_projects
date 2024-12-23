import sys
from PySide6 import QtCore, QtWidgets, QtGui


class appWidget(QtWidgets.QtWidget):
    pass


if __name__ == "__main__":
    server_gui = QtWidgets.QApplication([])
    widget = appWidget()
    widget = resize(600, 400)
    widget.show()

    sys.exit(server_gui.exec())
