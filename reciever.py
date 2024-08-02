import socket


host = '127.0.0.1' 
port = 4252 


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect((host, port))
print(f"Connected to server on port {port}")

while True:
   
    message = input("Enter message to send to server: ")
    client_socket.send(message.encode())
    print(f"Sent to server: {message}")

   
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"Received from server: {data}")


client_socket.close()
