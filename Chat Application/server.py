import socket
def start_server():
    host = '127.0.0.1'
    port = 9090
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"[SERVER] Chat server is running on {host}:{port}")
    print("[SERVER] Waiting for a connection...")
    conn, addr = server_socket.accept()
    print(f"[SERVER] Connected to {addr}")
    while True:
        message = conn.recv(1024).decode()
        if message.lower() == 'exit':
            print("[SERVER] Client has left the chat.")
            break
        print(f"Client: {message}")
        reply = input("You: ")
        conn.send(reply.encode())
        if reply.lower() == 'exit':
            print("[SERVER] Chat closed.")
            break
    conn.close()
    server_socket.close()
if __name__ == "__main__":
    start_server()