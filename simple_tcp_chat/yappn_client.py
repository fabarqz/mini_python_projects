import socket
import threading

username = input("Choose your user name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
        except:
            print("An error occured in sending the message")
            client.close()
