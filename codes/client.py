import socket
import math
import time

def complex_calculation(n):
    """Melakukan perhitungan kompleks, misalnya faktorial."""
    time.sleep(1)  # Simulasi waktu proses
    return math.factorial(n)

def simple_calculation(a, b):
    """Melakukan perhitungan sederhana, misalnya penjumlahan."""
    time.sleep(0.5)  # Simulasi waktu proses
    return a + b

def send_request_to_broker(message, app_id="Short"):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 8080))
    
    if app_id == "Long":
        # Melakukan perhitungan kompleks sebelum mengirim
        result = complex_calculation(5)  # Contoh: menghitung 5!
        formatted_message = f"{app_id}:{message}. Result: {result}"
    else:  # Default ke Short
        # Melakukan perhitungan sederhana sebelum mengirim
        result = simple_calculation(3, 4)  # Contoh: 3 + 4
        formatted_message = f"{app_id}:{message}. Result: {result}"

    client_socket.send(formatted_message.encode())
    client_socket.close()

if __name__ == "__main__":
    send_request_to_broker("This is a test request for long computation", "Long")
    send_request_to_broker("This is a test request for short computation", "Short")
