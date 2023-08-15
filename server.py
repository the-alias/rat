import socket

def main():

    msg_to_send = [
        '''systeminfo''',
        '''systeminfo | findstr /B /C:"OS Name" /C:"OS Version" #Get only that information''',
        '''wmic qfe get Caption,Description,HotFixID,InstalledOn #Patches''',
        '''wmic os get osarchitecture || echo %PROCESSOR_ARCHITECTURE% #Get system architecture''',
        '''[System.Environment]::OSVersion.Version #Current OS version''','''Get-WmiObject -query 'select * from win32_quickfixengineering' | foreach {$_.hotfixid} #List all patches''',
        '''Get-Hotfix -description "Security update" #List only "Security Update" patches'''
    ]
    host = 'localhost'
    port = 8080
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    conn, addr = server_socket.accept()
    for comm in msg_to_send:
        with open(comm[0:11]+".txt", 'w') as file:
            conn.sendall(comm.encode())
            
            data =conn.recv(1024).decode()
            
            file.write(data + '\n')
    conn.close()
    
if __name__ == "__main__":
    main()