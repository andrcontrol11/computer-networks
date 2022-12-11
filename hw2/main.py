import argparse
import subprocess

HEADERS_SIZE = 28
PARSER = argparse.ArgumentParser()
PARSER.add_argument("host")

INPUT_ARGS = PARSER.parse_args()

HOST: str = INPUT_ARGS.host


def check_host(host: str):
    if host[:5] == 'http:' or host[:6] == 'https:' or ':' in host:
        print(f"Bad host format for {host}")
        exit(1)
    host_split = host.split('.')
    if len(host_split) == 4:
        for num in host_split:
            if num == '' or num > '255' or num < '0':
                print(f"Bad host format for {host}")
                exit(1)
    elif len(host_split) != 2:
        print(f"Bad host format for {host}")
        exit(1)

check_host(HOST)
print('Checked host format.')

ICMP = subprocess.run(
    ["cat", "/proc/sys/net/ipv4/icmp_echo_ignore_all"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)

if ICMP.stdout == 1:
    print("ISCMP is disabled.")
    exit(1)

print("ICMP is enabled.")


print("Searching MTU...")

left, right = 0, 9001 - HEADERS_SIZE

while left + 1 < right:
    mid = (left + right) // 2

    ping = subprocess.run(
        ["ping", HOST, "-M", "do", "-s", str(mid), "-c", "3"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    if ping.returncode == 0:
        left = mid

    elif ping.returncode == 1:
        right = mid

    else:
        exit(ping.stderr)

print("MTU =", left + HEADERS_SIZE)