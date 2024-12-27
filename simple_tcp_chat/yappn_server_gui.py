import sys
from PySide6 import QtCore, QtWidgets, QtGui
import threading
import socket

local_host = "127.0.0.1"
port = 65469

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((local_host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast("{} left!".format(nickname).encode("ascii"))
            nicknames.remove(nickname)
            break


class appWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QtWidgets.QHBoxLayout(self)

        self.startServer = QtWidgets.QPushButton("Start Server")

        self.mainLayout.addWidget(self.startServer)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    server_gui = QtWidgets.QApplication([])
    widget = appWidget()
    widget.resize(600, 400)
    widget.show()

    sys.exit(server_gui.exec())
