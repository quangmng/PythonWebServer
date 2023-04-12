# import socket module
# insert < 8 lines of code - remove me before submission.
from socket import *
import sys  # Terminate prog.
import threading  # multithreading

# Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(("192.168.0.2", serverPort))


# Fill in end

def handle_client(conn, addr):
    global message
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            # Send one HTTP header line into socket
            message = connectionSocket.recvfrom(1024).decode()
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())
                connectionSocket.close()

        except IOError:
            # Send response message for file not found
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("<html><head>404 Not Found</head><body></body></html>\r\n".encode())
            connectionSocket.close()

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
    serverSocket.close()


def start():
    serverSocket.listen()
    print('Ready to serve...')
    while True:
        # Establish the connection
        conn, addr = serverSocket.accept()
        connectionSocket, addr = serverSocket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()
sys.exit()  # Terminate the program after sending the corresponding data
