#  _   _  _____  _____ __        __  ___   ____   _  __   ____    ____     _     _   _ 
# | \ | || ____||_   _|\ \      / / / _ \ |  _ \ | |/ /  / ___|  / ___|   / \   | \ | |
# |  \| ||  _|    | |   \ \ /\ / / | | | || |_) || ' /   \___ \ | |      / _ \  |  \| |
# | |\  || |___   | |    \ V  V /  | |_| ||  _ < | . \    ___) || |___  / ___ \ | |\  |
# |_| \_||_____|  |_|     \_/\_/    \___/ |_| \_\|_|\_\  |____/  \____|/_/   \_\|_| \_|

import os
import socket
import time
import sys

def Scan():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        myIP = s.getsockname()[0]
        s.close()

        basIP = ".".join(myIP.split(".")[:-1]) + "."
        print(f"\nDetected network: {basIP}X")

        is_windows = os.name == 'nt'

        zabraneIP = []
        for i in range(1, 256):
            targetIP = basIP + str(i)
        
            if is_windows:
                cmd = f"ping -n 1 -w 300 {targetIP} > nul"

            else:
                cmd = f"ping -c 1 -W 1 {targetIP} > /dev/null 2>&1"
            
            response = os.system(cmd)
            time.sleep(0.05)

            
            if response == 0:
                try:
                    name = socket.gethostbyaddr(targetIP)[0]
                    print(f"IP {targetIP} is ACTIVE - {name}")
                    zabraneIP.append(f"{targetIP} | {name}")
                except socket.herror:
                    print(f"IP {targetIP} is ACTIVE - Name: Unknown")
                    zabraneIP.append(f"{targetIP} | Unknown")
            else:
                print(f"Checking: {targetIP}", end="\r")

        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))

        reports_dir = os.path.join(application_path, "reports")

        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)

        filename = os.path.join(reports_dir, "network_scan_report.txt")

        
        with open(filename, "w") as f:
            f.write("--- NETWORK SCAN REPORT --- \n\n")
            f.write(f"DATE: {time.ctime()}\n")
            f.write(f"TARGET IP: {basIP}X\n\n")

            if zabraneIP:
                for i in zabraneIP:
                    f.write(f"[+] {i}\n")
                f.write(f"\n{len(zabraneIP)} active IPs found.")
            else:
                f.write(f"No active IPs found.")
        
        print(f"\n\nScan completed, report saved in {filename}")
    
    except Exception as e:
        print(f"There was an error. - {e}")