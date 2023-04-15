# import socket module
from socket import *
import sys  # Terminate prog.
import threading  # multithreading

# Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(("192.168.0.2", serverPort))


def start():
    serverSocket.listen()
    print('Ready to serve...')
    while True:
        # Establish the connection
        conn, addr = serverSocket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


def handle_client(conn, addr):
    global message

    print(f"[NEW CONNECTION] {addr} connected.")
    try:
        message = conn.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:], 'r')
        outputdata = f.read()

        # Send one HTTP header line into socket
        conn.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        conn.send("\r\n".encode())
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            conn.send(outputdata[i].encode())
        conn.send("\r\n".encode())

    except IOError:
        # Send response message for file not found
        conn.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        conn.send("<html><title>404 Not Found</title><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        conn.close()

    # Close client socket
    conn.close()


print("[STARTING] server is starting...")
start()
sys.exit()  # Terminate the program after sending the corresponding data
