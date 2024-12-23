from socket import socket, AF_INET, SOCK_STREAM

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 5050

    server_socket = socket(family=AF_INET, type=SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print("Listening!")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        msg = conn.recv(1024)
        if not msg:
            break
        decoded_msg = msg.decode("utf-8")
        print(decoded_msg)

    conn.close()
