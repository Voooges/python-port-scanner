# Python TCP Port Scanner

A beginner Python project that checks selected TCP ports on
127.0.0.1 using Python's socket library.

## What I practiced

- Creating IPv4 TCP sockets
- Setting connection timeouts
- Handling refused connections and other network errors
- Reading command-line arguments with argparse
- Validating port numbers
- Comparing results with an Nmap TCP connect scan

## Requirements

- Python 3
- Nmap for comparison testing

No external Python packages are required.

## Run the scanner

```bash
python3 scanner.py --ports 7999 8000 8001
```

View help:

```bash
python3 scanner.py --help
```

## Test setup

I tested this project inside a Kali Linux virtual machine.

In one terminal, start a local HTTP server from the project folder:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Keep the server running and run the scanner in another terminal.

## Observed output

With the server running:

```text
Scanning 127.0.0.1

Port 7999: CLOSED — connection refused
Port 8000: OPEN
Port 8001: CLOSED — connection refused
```

After stopping the server with Ctrl+C, all three ports
reported CLOSED — connection refused.

## Nmap comparison

```bash
nmap -sT -Pn -n -p 7999,8000,8001 127.0.0.1
```

Both tools reported port 8000 open while the server was running
and ports 7999 and 8001 closed.

## Input validation

```bash
python3 scanner.py --ports 70000
```

The scanner rejected this input because valid port numbers
must be between 1 and 65535.

## Limitations

- The target is fixed to IPv4 localhost, 127.0.0.1.
- Ports are checked sequentially using a one-second timeout.
- A timeout does not establish whether a port is closed or filtered.
- An open port means a TCP connection succeeded at scan time.
- The scanner does not identify services or detect vulnerabilities.
- Timeout and general network-error handling are implemented,
  but these paths have not yet been deliberately tested.
- Results can change when services start or stop.

## Learning context

I built this project with guided assistance and tested it
in my own local lab. It is a learning tool, not a replacement
for Nmap.
