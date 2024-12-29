#!/usr/bin/python3

import sys
import socket

def check_port_status(ip, port):
    """Checks if a port is open on the given IP address.

    Args:
        ip: The IP address to check.
        port: The port number to check.

    Returns:
        True if the port is open, False otherwise.
    """
    try:
        with socket.socket() as s:
            s.settimeout(1)
            s.connect((ip, port))
            return True
    except (ConnectionRefusedError, socket.timeout):
        return False

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <ip> [start_port] [end_port]", file=sys.stderr)
    exit(1)

ip = sys.argv[1]
start_port = 1
end_port = 65535

if len(sys.argv) >= 3:
    start_port = int(sys.argv[2])
if len(sys.argv) >= 4:
    end_port = int(sys.argv[3])

for port in range(start_port, end_port + 1):
    if check_port_status(ip, port):
        print(f"Open port found: {port}")