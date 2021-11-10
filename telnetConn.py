import sys
import telnetlib
import time
import getpass
import ctypes
import socket

def shut_down_sockets(tn):
    tn.get_socket().shutdown(socket.SHUT_WR)
    data = tn.read_all().decode('ascii')
    tn.close()

def telnetConnection(host, username, password, number, inputText):


    print('Connection started... \nHost: %s\nUsername: %s\nPassword: %s\nMessage: %s\nText %s'%(host, username, password, number, inputText))
    HOST = host
    user = username
    password = password
    tn = telnetlib.Telnet(HOST)
    try:
        

        print("Connection Established...")

        tn.read_until(b"login: ", timeout = 5)
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ", timeout = 5)
            tn.write(password.encode('ascii') + b"\n")

        ctypes.windll.user32.MessageBoxW(0, "Login Successful.", "Aawwwyyyy yeah", 1)
        #print("Login Successful.")
    except Exception as e:
        shut_down_sockets(tn)
        ctypes.windll.user32.MessageBoxW(0, "Oh snap! %s happened"%(e.__class__,), "Error", 1)
    try:
        send_msg = "wan lte send"
        ctypes.windll.user32.MessageBoxW(0, "Sending Message....", "BBBAAAZZZINNNGGAAAA", 1)
        #print("Sending Message...\n")
        command = f"{send_msg} {number} {inputText}"
        response = f"Send {inputText} to {number}"
        time.sleep(1) 
        #tn.write(command.encode('ascii')+b"\n")
        #tn.read_until(response.encode('ascii'), timeout = 5)
        ctypes.windll.user32.MessageBoxW(0, "Message to %s sent.\n"%(number), "oooohhhh booooyyyy", 1)
        tn.write(b"ls\n")
        tn.write(b"exit\n")
        ctypes.windll.user32.MessageBoxW(0, "Telnet connection closed", "NANANANANA BATMAN", 1)
        #print("Telnet connection closed\n")
    except Exception as e:
        shut_down_sockets(tn)
        ctypes.windll.user32.MessageBoxW(0, "Oh snap! %s happened"%(e.__class__,), "Error", 1)
    
    # tn.write(b"ls\n")
    # tn.write(b"exit\n")

    # print(tn.read_all().decode('ascii'))

