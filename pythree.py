import socket
import threading
import random

# array  for qoutes
qoutes = ["We cannot solve problems with the kind of thinking we employed when we came up with them.","Learn as if you will live forever, live like you're gonna die tommorow.",
	   "When you give joy to others, you get more joy in return.", "When you change your thoughts, remember that you will change the world."]

def handle_client(client_socket):
	#retrieving random qoute from the array
	qoute =  random.choice(qoutes)
	#send the qoute to the client
	client_socket.send(qoute.encode())
	#close the client socket
	client_socket.close()

def main():
	#creating TCP socket
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#bind the socket to your localhost and port 8888
	server_socket.bind(("", 8888))

	#listen for incoming connections
	server_socket.listen(5)
	while True:
		#accepting a client connection
		client_socket, address = server_socket.accept()
		print("[*] Accepted connection from {}:{}".format(address[0], address[1]))
		#create a new thread to handle the client
		client_handler = threading.Thread(target=handle_client, args=(client_socket,))
		client_handler.start()

if __name__ == "__main__":
	main()

