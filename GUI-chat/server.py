import socket
import threading

HOST = "127.0.0.1"
PORT = "1234"
LISTENER_LIMIT = 5


def main():
    # Socket class object
    # AF_INET: Ipv4 addresses
    # SOCK_STREAM: TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Server is running on host {HOST} and port {PORT}")
    except ConnectionError:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    # Listening to server limit
    server.listen(LISTENER_LIMIT)

    # Keep listening to client connections
    while 1:
        client, address = server.accept()
        print(f"Successfully connect to client {address[0]} {address[1]}")


if __name__ == '__main__':
    main()
