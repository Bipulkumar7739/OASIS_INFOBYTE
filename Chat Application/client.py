import socket
def start_client():
    host = '127.0.0.1'
    port = 9090
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"[CLIENT] Connected to chat server at {host}:{port}")
    print("[CLIENT] Type 'exit' to leave the chat.\n")
    while True:
        message = input("You: ")
        client_socket.send(message.encode())
        if message.lower() == 'exit':
            print("[CLIENT] Exiting chat.")
            break
        reply = client_socket.recv(1024).decode()
        if reply.lower() == 'exit':
            print("[CLIENT] Server ended the chat.")
            break
        print(f"Server: {reply}")
    client_socket.close()
if __name__ == "__main__":
    start_client()