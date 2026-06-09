# Network Scanner

A lightweight ICMP-based host discovery tool written in Python. Takes a subnet in CIDR notation, pings each usable host address, and reports which hosts are alive.

Built as part of a penetration testing assessment at Holmesglen Institute (Certificate IV in Information Technology).

---

## Features

- Accepts any valid CIDR subnet (e.g. `192.168.1.0/24`, `10.0.0.0/16`)
- Defaults to `/24` if no prefix is provided
- Validates subnet input and rejects invalid entries
- Sends 2 ICMP packets per host with a 1-second timeout
- Displays live hosts in real time as they are discovered
- Prints a full summary on scan completion
- No third-party dependencies — standard library only

---

## Requirements

- Python 3
- Linux (tested on Kali Linux)
- No additional packages required (`ipaddress` and `subprocess` are standard library)

---

## Usage

```bash
python3 Network_Scanner.py
```

When prompted, enter a subnet:

```
Enter a subnet (e.g. 192.168.1.0/24) or IP address (defaults to /24): 192.168.15.0/24
```

---

## Example Output

```
Total number of available hosts in your subnet: 254
CIDR notation used: 192.168.15.0/24
pinging in progress...
192.168.15.1 is alive and responding
192.168.15.128 is alive and responding
192.168.15.129 is alive and responding

Scan complete
Total number of live hosts: 3 out of 254
[LIVE] 192.168.15.1
[LIVE] 192.168.15.128
[LIVE] 192.168.15.129
```

---

## How it works

The script runs in four stages:

1. **Input handling** — prompts the user for a subnet, defaults to `/24` if no prefix given, validates using Python's `ipaddress` module
2. **Host enumeration** — expands the subnet into individual host addresses, excluding the network and broadcast addresses
3. **Scanning** — pings each host via the system `ping` command using `subprocess`, records hosts that respond
4. **Output** — prints a real-time feed of live hosts during the scan, followed by a full summary

---

## Known Limitations

This tool uses ICMP echo requests (ping) for host discovery. The verification baseline for this assessment used `arp-scan`, which operates at layer 2 using ARP. Because ARP requests are not typically filtered by host firewalls, `arp-scan` may discover hosts that this scanner misses. Any discrepancy between the two tools is an expected protocol-level difference, not a bug.

For more reliable local subnet discovery, an ARP-based approach using `scapy` would be more accurate, but requires root privileges and a third-party library. The ICMP approach was chosen deliberately for its simplicity and zero external dependencies.

---

## Ethical and Legal Notice

This tool is intended for use on networks you own or have explicit written permission to scan. Unauthorised scanning of networks is illegal in most jurisdictions. Always obtain proper authorisation before running any network scanning tool.

---

## Author

Aviv Gafni
Certificate IV in Information Technology — Holmesglen Institute
