#!/usr/bin/python3

from argparse import ArgumentParser
import socket
from threading import Thread
from time import time

open_ports = []

def prepare_args():
    parser = ArgumentParser(description="Fast Port Scanner")
    parser.add_argument("ip", help="host to scan")
    parser.add_argument("-s", "--start", type=int, default=1, help="starting port")
    parser.add_argument("-e", "--end", type=int, default=65535, help="ending port")
    parser.add_argument("-t", "--threads", type=int, default=500, help="threads to use")
    parser.add_argument("-V", "--verbose", action="store_true", help="verbose output")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")
    return parser.parse_args()

def prepare_ports(start, end):
    for port in range(start, end + 1):
        yield port

def scan_port():
    while True:
        try:
            with socket.socket() as s:
                s.settimeout(1)
                port = next(ports)
                s.connect((arguments.ip, port))
                open_ports.append(port)
                if arguments.verbose:
                    print(f"\r{open_ports}", end="")
        except (ConnectionRefusedError, socket.timeout):
            pass
        except StopIteration:
            break

def prepare_threads(threads):
    thread_list = [Thread(target=scan_port) for _ in range(threads + 1)]
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    arguments = prepare_args()
    ports = prepare_ports(arguments.start, arguments.end)
    start_time = time()
    prepare_threads(arguments.threads)
    end_time = time()
    if arguments.verbose:
        print()
    print(f"Open Ports Found {open_ports}")
    print(f"Time Taken {round(end_time - start_time, 2)}")