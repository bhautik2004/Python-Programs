import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),80))
server_socket.listen(5)
print("Request Listning...")
