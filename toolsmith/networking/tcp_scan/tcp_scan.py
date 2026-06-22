import sys
import socket

host = sys.argv[1]
ports = [22, 80, 443, 4212]


def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        sock.connect((host, port))
        print(f"{host}:{port} open")
    except ConnectionRefusedError:
        print(f"{host}:{port} closed")
    except socket.timeout:
        print(f"{host}:{port} timeout")
    finally:
        sock.close()


for port in ports:
    scan_port(host, port)
