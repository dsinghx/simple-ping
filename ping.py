import time
from datetime import datetime
from icmplib import ping, traceroute
from colorama import Fore, Style, init
from prettytable import PrettyTable

# Initialize colorama
init()

# Replace with your list of IP addresses
ip_addresses = ["8.8.4.4", "8.8.8.8"]

def trace_ips(ip_addresses):
    table = PrettyTable()
    table.field_names = ["Timestamp", "IP", "Status", "Path"]

    for ip in ip_addresses:
        try:
            ping_result = ping(ip, count=1, timeout=2)
            if ping_result.is_alive:
                status = Fore.GREEN + "OK" + Style.RESET_ALL
            else:
                status = Fore.RED + "Timeout" + Style.RESET_ALL

            traceroute_result = traceroute(ip)
            path = " -> ".join([hop.address for hop in traceroute_result])

        except Exception as e:
            status = Fore.RED + "Error: " + str(e) + Style.RESET_ALL
            path = ""

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        table.add_row([current_time, ip, status, path])

    print(table)

while True:
    trace_ips(ip_addresses)
    time.sleep(5)