# worker_server.py
import socket

def start_worker_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", port))
    server_socket.listen()
    print(f"Worker server running on port {port}")

    while True:
        client_socket, address = server_socket.accept()
        data = client_socket.recv(1024).decode()
        print(f"Worker on port {port} received request: {data}")
        client_socket.close()

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1])
    start_worker_server(port)
