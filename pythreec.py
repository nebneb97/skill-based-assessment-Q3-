import socket

HOST ="10.0.2.15"
PORT =  8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	data = s.recv(1024)
	print("Received qoute:", data.decode())
