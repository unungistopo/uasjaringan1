import socket
import sys
import threading

# Daftar worker server dan port mereka
worker_servers = [("localhost", 8081), ("localhost", 8082), ("localhost", 8083)]
worker_count = len(worker_servers)
worker_load = [0] * worker_count  # Untuk melacak jumlah request yang diterima setiap worker
current_worker = 0  # Indeks worker yang akan menerima request berikutnya

def start_broker_server(port, method):
    global current_worker

    broker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    broker_socket.bind(("localhost", port))
    broker_socket.listen()
    print(f"Broker server running on port {port} using method {method}")

    while True:
        client_socket, client_address = broker_socket.accept()
        data = client_socket.recv(1024).decode()

        # Pendekatan distribusi request
        if method == "1":
            # Pemerataan jumlah request (Pendekatan 1)
            min_load_index = worker_load.index(min(worker_load))
            worker_host, worker_port = worker_servers[min_load_index]
            worker_load[min_load_index] += 1  # Update load counter
        elif method == "2":
            # Berurutan sesuai server-id (Pendekatan 2)
            worker_host, worker_port = worker_servers[current_worker]
            current_worker = (current_worker + 1) % worker_count

        # Meneruskan request ke worker server yang dipilih
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as worker_socket:
            worker_socket.connect((worker_host, worker_port))
            worker_socket.sendall(data.encode())
            print(f"Broker forwarded request '{data}' to worker on port {worker_port}")
        
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python broker_server.py <broker_port> <method>")
        print("Method 1: Equal load distribution")
        print("Method 2: Round-robin based on server ID")
        sys.exit(1)

    broker_port = int(sys.argv[1])
    method = sys.argv[2]  # Choose method 1 or 2
    start_broker_server(broker_port, method)
