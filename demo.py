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