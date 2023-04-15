from socket import *

serverName = '192.168.0.2'
serverPort = 6789

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Request a file from the server
filename = 'HelloWorld.html'
request = f"GET /{filename} HTTP/1.1\r\nHost: {serverName}\r\n\r\n"
clientSocket.send(request.encode())

# Receive the response from the server
response = b''
while True:
    data = clientSocket.recv(1024)
    if not data:
        break
    response += data
print(response.decode())

clientSocket.close()
