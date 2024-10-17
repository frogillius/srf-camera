import socket

def send_command(command, host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Sending command: {command}")
        client_socket.sendall(command.encode())

        response = client_socket.recv(1024)
        print(f"Received response: {response.decode()}")

if __name__ == "__main__":
    commands = [
        "gimme front",
        "gimme back",
        "gimme left",
        "gimme right",
        "invalid command"
    ]
    
    for cmd in commands:
        send_command(cmd)
