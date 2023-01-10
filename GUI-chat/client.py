import socket
import threading

HOST = "127.0.0.1"
PORT = 1234


def main():
    # Socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    try:
        client.connect((HOST, PORT))
        print(f"Successfully connected to the server")
    except ConnectionError:
        print(f"Unable to connect to host {HOST} and port {PORT}")


if __name__ == '__main__':
    main()
