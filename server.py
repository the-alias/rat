import socket

def main():

    host = 'localhost'
    port = 8080
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    conn, addr = server_socket.accept()
    with open("output.txt", 'w') as file:
            data =conn.recv(1048576).decode()      
            file.write(data + '\n')
    conn.close()
    
if __name__ == "__main__":
    main()