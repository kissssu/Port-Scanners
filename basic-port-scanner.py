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

open_ports = []  # Store open ports
total_ports = end_port - start_port + 1 # Calculate the total number of ports to be scanned

for port in range(start_port, end_port + 1):
    if check_port_status(ip, port):
        open_ports.append(port)

print(f"Scan Results for {ip}:")
print(f"\nTotal Ports Scanned: {total_ports}") # Print the total number of ports scanned
print(f"Open Ports Found: {len(open_ports)}\n")

if open_ports:
    print("Open Ports:")
    for port in open_ports:
        print(f"- {port}")
else:
    print("No open ports found.")
