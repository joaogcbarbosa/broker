from socket import socket, AF_INET, SOCK_STREAM
from time import sleep


if __name__ == "__main__":
    SERVER_HOST, SERVER_PORT = "127.0.0.1", 5050

    client_socket = socket(family=AF_INET, type=SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    counter = 1
    while True:
        msg = input("Mensagem: ")
        client_socket.send(msg.encode("utf-8"))
        counter += 1
