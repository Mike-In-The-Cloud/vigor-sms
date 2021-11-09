import sys
import telnetlib
import time
import getpass

def telnetConnection(host, username, password, number, inputText):


    print('Connection started, \nHost: %s\nUsername: %s\nPassword: %s\nMessage: %s\nText %s'%(host, username, password, number, inputText))
    
    try:
        HOST = host
        # user = username
        # password = password
        #tn = telnetlib.Telnet(HOST)

        print("Connection Established...")

        # tn.read_until(b"login: ")
        # tn.write(user.encode('ascii') + b"\n")
        # if password:
        #     tn.read_until(b"Password: ")
        #     tn.write(password.encode('ascii') + b"\n")

        print("Login Successful.")
    except Exception as e:
        print("Oh snap! %s happened"%(e.__class__,))
    
    
    try:
        send_msg = "wan lte send"
        print("Sending Message...")
        time.sleep(1) 
        #tn.write("%s %s %s"%(snd_msg, number, inputText))
        #tn.read_until("Send [%s] to [%s]"%(inputText, number))
        print("Message to %s sent."%(number))
        #tn.write("exit")
        print("Telnet connection closed")
    except Exception as e:
        print("Oh snap! %s happened"%(e.__class__,))

    # tn.write(b"ls\n")
    # tn.write(b"exit\n")

    # print(tn.read_all().decode('ascii'))