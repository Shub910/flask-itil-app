import socket


host = '127.0.0.1'  # localhost
port = 4252  # Port number


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind((host, port))


server_socket.listen(1)
print(f"Socket server listening on port {port}")


conn, addr = server_socket.accept()
print(f"Connection from {addr}")

while True:
    
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Received from client: {data}")

    
    message = input("Enter message to send to client: ")
    conn.send(message.encode())
    print(f"Sent to client: {message}")


conn.close()
