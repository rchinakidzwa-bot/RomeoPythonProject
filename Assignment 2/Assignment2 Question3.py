import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = None

try:
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow the address to be reused
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the server to an IP address and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen(1)

    print(f"Server is listening on {HOST}:{PORT}")

    # Accept a client connection
    client_socket, client_address = server_socket.accept()

    with client_socket:
        print("Connected to client:", client_address)

        # Receive a maximum of 1024 bytes
        data = client_socket.recv(1024)

        if data:
            message = data.decode("utf-8")
            print("Message received:", message)

            # Send a response to the client
            client_socket.sendall(
                "Message received successfully.".encode("utf-8"))
        else:
            print("No data was received from the client.")

except ConnectionError as error:
    print("A connection error occurred:", error)

except OSError as error:
    print("A network error occurred:", error)

finally:
    if server_socket is not None:
        server_socket.close()
        print("Server socket closed.")




