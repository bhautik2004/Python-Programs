import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("www.google.com",80))
print("Requested URL is Connected...")
