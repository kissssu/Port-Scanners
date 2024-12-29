# Python Port Scanners

This folder contains two Python scripts for port scanning:

- ```Basic_Port_Scanner.py```: This is a simple script that scans a specified IP address for open ports within a given range.

- ```Advanced_Port_Scanner.py```: This is a more advanced script that utilizes multithreading for faster scanning and offers additional features like verbose output and custom thread count.

## Understanding Port Scanning
Port scanning is a network security technique used to identify open ports on a host. Each port corresponds to a specific service or application running on the machine. By scanning for open ports, you can potentially discover vulnerabilities or gain insights into the services available on a host.

**Important Note**: Port scanning should only be performed on networks where you have explicit permission. Unauthorized scanning is a violation of security policies and may be illegal.
 
## Usage

#### Basic_Port_Scanner.py:

```
python Basic_Port_Scanner.py <IP_ADDRESS> [START_PORT] [END_PORT]
```
1. <IP_ADDRESS>: The IP address of the host to scan.
2. [START_PORT]: (Optional) The starting port number (defaults to 1).
3. [END_PORT]: (Optional) The ending port number (defaults to 65535).

#### Advanced_Port_Scanner.py:

```
python Advanced_Port_Scanner.py <IP_ADDRESS> [OPTIONS]
```
1. <IP_ADDRESS>: The IP address of the host to scan.
2. [OPTIONS]:
- -s, --start: (Optional) The starting port number (defaults to 1).
- -e, --end: (Optional) The ending port number (defaults to 65535).
- -t, --threads: (Optional) The number of threads to use (defaults to 500).
- -V, --verbose: Enables verbose output, displaying open ports as they are found.
- -v, --version: Displays the script version.

## Example Usage

#### Basic Scanner:

```
python Basic_Port_Scanner.py 192.168.1.100
```
- This will scan the host 192.168.1.100 for open ports between ports 1 and 65535.

#### Advanced Scanner:

```
python Advanced_Port_Scanner.py 10.0.0.1 -s 80 -e 443 -t 100 -V
```

- This will scan the host 10.0.0.1 for open ports between ports 80 and 443 using 100 threads and displaying open ports as they are found.

## Disclaimer

These scripts are provided for educational purposes only. Please be mindful of network security and only scan hosts with proper permission. Scanning unauthorized systems is a violation of security policies and may be illegal.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit pull requests with 1  improvements or additional features. Make sure your code adheres to PEP 8 style guidelines for readability. 

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
