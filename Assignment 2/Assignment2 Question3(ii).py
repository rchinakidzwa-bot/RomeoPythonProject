import socket

HOST = "127.0.0.1"
PORT = 5000

try:
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        client_socket.connect((HOST, PORT))

        message = "Hello from client!"

        # Send the message
        client_socket.sendall(message.encode("utf-8"))
        print("Message sent:", message)

        # Receive the server's response
        response = client_socket.recv(1024)

        print("Server response:", response.decode("utf-8"))

except ConnectionRefusedError:
    print("Connection refused. Make sure the server is running.")

except ConnectionError as error:
    print("A connection error occurred:", error)

except OSError as error:
    print("A network error occurred:", error)