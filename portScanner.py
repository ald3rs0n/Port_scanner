import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(5)
host = input("Please enter the IP: ")
port = int(input("Please enter the PORT: "))

def portScanner(host,port):
    if s.connect_ex((host,port)):
        print("Port is closed")
    else:
        print("Port is open")

portScanner(host,port)