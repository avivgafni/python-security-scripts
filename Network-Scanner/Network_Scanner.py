# Network scanner tool
# Author - Aviv Gafni

import ipaddress # Parses and validates CIDR subnet input, enumerates host addresses
import subprocess # Executes system ping command to test host reachability

# Function: ping a single host and return True if alive, False if not
def ping_host(host):
    # Send 2 pings, timeout 1 second for reply, capture output to keep terminal clean
    ping = subprocess.run(['ping', '-c', '2', '-n', '-W', '1', str(host)], capture_output=True, text=True)
    if ping.returncode == 0:  # Return code 0 = host responded, non-zero = no response
        return True
    else:
        return False

# Stage 1: Input handling
# Loop until the user enters a valid subnet

while True:
    subnet = input("Enter a subnet (e.g. 192.168.1.0/24) or IP address (defaults to /24): ")
    if "/" not in subnet: # If no prefix given, default to /24
        subnet = subnet + "/" + "24"

    # Parse and validate the subnet using ipaddress module
    # strict=False allows host bits to be set (e.g. 192.168.1.5/24 is treated as 192.168.1.0/24)
    try:
        cidr = ipaddress.ip_network(subnet, strict=False)
        break # Valid subnet entered, exit the loop
    except ValueError:
        print("Invalid CIDR IP address") # Reject invalid input and prompt again

# Stage 2: Host enumeration

hosts = list(cidr.hosts())  # Insert into memory a list of all usable host addresses, excluding network and broadcast
count_hosts = len(hosts)  # Count usable host addresses, excluding network and broadcast


# Inform the user of scan input details before starting
print(f"\nTotal number of available hosts in your subnet: {count_hosts}")
print(f"CIDR notation used: {cidr}")

# Stage 3: Scanning
live_host_count = 0 # initiate counter - number of live hosts
live_hosts = [] # List to store responding host addresses

print("pinging in progress...")

# Loop through each host address and ping it
for host in hosts:
    result = ping_host(host)  # Call ping function, returns True or False
    if result:                # Host responded
        live_host_count += 1
        live_hosts.append(host)
        print(f"{host} is alive and responding")


# Stage 4: Output summary
print("\nScan complete")
print(f"Total number of live hosts: {live_host_count} out of {count_hosts}")

# Print final list of all discovered live hosts
for live in live_hosts:
    print(f"[LIVE] {live}")
