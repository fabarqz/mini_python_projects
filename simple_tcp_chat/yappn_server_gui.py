import sys
import subprocess
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


def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode("ascii"))
        client.send("Connected to server!".encode("ascii"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


class appWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QtWidgets.QVBoxLayout(self)

        self.status_label = QtWidgets.QLabel("Server is not running", self)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(self.status_label)
        self.startServer = QtWidgets.QPushButton("Start Server")
        self.startServer.clicked.connect(self.start_server)
        self.mainLayout.addWidget(self.startServer)
        self.startClient_one = QtWidgets.QPushButton("Start Client 1")
        self.startClient_one.clicked.connect(self.run_client)
        self.mainLayout.addWidget(self.startClient_one)
        self.startClient_two = QtWidgets.QPushButton("Start Client 2")
        self.startClient_two.clicked.connect(self.run_client)
        self.mainLayout.addWidget(self.startClient_two)

        self.setLayout(self.mainLayout)

    def start_server(self):
        self.server_thread = threading.Thread(target=receive)
        self.server_thread.daemon = True
        self.server_thread.start()
        self.status_label.setText("Server is running")

    def run_client(self):
        try:
            command = 'start cmd /k "cd "simple_tcp_chat" & python yappn_client.py"'
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"An error occuerd:{e}")


if __name__ == "__main__":
    server_gui = QtWidgets.QApplication([])
    widget = appWidget()
    widget.resize(600, 400)
    widget.show()

    sys.exit(server_gui.exec())
