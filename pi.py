import socket

import camData

def start_server(host='0.0.0.0', port=65432):
	# Create a TCP/IP socket
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind((host, port))
	server_socket.listen()

	print(f"Listening for connections on {host}:{port}...")

	while True:
		# Wait for a connection
		connection, client_address = server_socket.accept()
		try:
			print(f"Connection from {client_address}")

			while True:
				# Receive the data
				data = connection.recv(1024)
				if not data:
					response = "bad packet"
					connection.sendall(response.encode())
				decoded = data.decode()
				print(f"Received: {decoded}")
				if decoded=="gimme front":
					camData.get_front_data()
				elif decoded=="gimme back":
					camData.get_back_data()
				elif decoded=="gimme left":
					camData.get_left_data()
				elif decoded=="gimme right":
					camData.get_right_data()
				else:
					# Send back an arbitrary response (for example)
					response = "Recieved but no data"
					connection.sendall(response.encode())
				break
		finally:
			# Clean up the connection
			connection.close()

if __name__ == "__main__":
	start_server()