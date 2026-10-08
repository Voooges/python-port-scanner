import argparse
import socket

parser = argparse.ArgumentParser(
    description="Scan TCP ports on your local machine."
)
parser.add_argument(
    "--ports",
    nargs="+",
    type=int,
    required=True,
    help="Ports to scan, separated by spaces"
)
args = parser.parse_args()

if any(port < 1 or port > 65535 for port in args.ports):
    parser.error("Ports must be between 1 and 65535.")

target = "127.0.0.1"
print(f"Scanning {target}\n")

for port in args.ports:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
            connection.settimeout(1)
            connection.connect((target, port))
            print(f"Port {port}: OPEN")

    except ConnectionRefusedError:
        print(f"Port {port}: CLOSED — connection refused")

    except socket.timeout:
        print(f"Port {port}: TIMEOUT — no result within 1 second")

    except OSError as error:
        print(f"Port {port}: ERROR — {error}")
