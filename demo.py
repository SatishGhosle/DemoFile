import socket
import sys



def create_socket(add_fam = -1,tcp_protocol = -1):
    try:
        s = socket.socket(add_fam, tcp_protocol)
    except socket.error as err:
        print(f"Socket could not be created due to {err}")
    return s

def get_hostIP(host_name):
    try:
        hostIP = socket.gethostbyname(host_name)
    except socket.gaierror:
        print("Error occured while resolving the host")
        sys.exit()
    
    if hostIP:
        return hostIP

s = create_socket(socket.AF_INET, socket.SOCK_STREAM)

host = get_hostIP("www.cisco.com")

s.connect((host, 80))
print("Socket has successfully connected to {host}".format(host = host))



s1 = create_socket()
port = 1234
s1.bind(("",port))
print("socket binded to port = ",port)



s1.listen(5)
print("Scoket is listenining")

while True:
    c, addr = s1.accept()
    print("Established connection", addr)
    
    c.send(f"You have successfully connected to {addr}".encode())
    
    c.close()
    break

#Another Example

# socket object
s = socket.socket()        
 
# Port to connect
port = 12345               
 
# Connecting to the server
s.connect(('127.0.0.1', port))
 
# Receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.close()    
