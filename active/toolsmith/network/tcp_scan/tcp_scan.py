import sys
import socket

host = sys.argv[1]
ports = [21, 22, 53, 80, 443, 4212]
COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
}


def scan_port(host, port):
    service = COMMON_SERVICES.get(port, "UNKNOWN")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        sock.connect((host, port))
        print(f"{host}:{port} open ({service})")
    except ConnectionRefusedError:
        print(f"{host}:{port} closed ({service})")
    except socket.timeout:
        print(f"{host}:{port} timeout ({service})")
    finally:
        sock.close()


for port in ports:
    scan_port(host, port)
