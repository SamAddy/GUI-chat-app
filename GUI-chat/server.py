import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
# clients
active_clients = []
usernames = []


def listen_for_messages(client, username):
    """
    This function listens for any upcoming messages

    Param:
    client
    """
    while 1:
        message = client.recv(2048).decode('utf-8')

        if message != '':
            # If message isn't empty then final message should be in the format username ~ message
            # eg: Sam ~ Hello world!
            final_message = username + '~' + message
            broadcast_message(final_message)

        else:
            print(f"The message sent from client {username} is empty.")


def send_message_to_client(client, message):
    """
    This function forwards message to a specific client.
    """
    client.sendall(message.encode())


def broadcast_message(message):
    """"
    This function sends message to all active clients connected to the server.
    """

    for user in active_clients:
        # user.send(message)
        send_message_to_client(user[1], message)


def client_handler(client):
    """
    Server listens for client message
    Contain username
    """

    while 1:
        # Wait for any message from a specific client.
        username = client.recv(2048).decode('utf-8')
        if username != "":
            active_clients.append((username, client))
            usernames.append(username)
            notification = "SERVER~" + f"{username} just joined the chat."
            broadcast_message(notification)
            break
        else:
            print("Client username is empty")

    # Thread to get the socket to listen all the time.
    threading.Thread(target=listen_for_messages, args=(client, username,)).start()


def main():
    # Socket class object
    # AF_INET: Ipv4 addresses
    # SOCK_STREAM: TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Server is running on host {HOST}:{PORT}")
    except ConnectionError:
        print(f"Unable to bind to host {HOST}:{PORT}")

    # Listening to server limit
    server.listen()

    # Keep listening to client connections
    while 1:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")
        client.send('USER'.encode('utf-8'))
        # Thread is started when a client gets connected
        threading.Thread(target=client_handler, args=(client,)).start()


if __name__ == '__main__':
    main()
