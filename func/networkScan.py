#  _   _  _____  _____ __        __  ___   ____   _  __   ____    ____     _     _   _ 
# | \ | || ____||_   _|\ \      / / / _ \ |  _ \ | |/ /  / ___|  / ___|   / \   | \ | |
# |  \| ||  _|    | |   \ \ /\ / / | | | || |_) || ' /   \___ \ | |      / _ \  |  \| |
# | |\  || |___   | |    \ V  V /  | |_| ||  _ < | . \    ___) || |___  / ___ \ | |\  |
# |_| \_||_____|  |_|     \_/\_/    \___/ |_| \_\|_|\_\  |____/  \____|/_/   \_\|_| \_|

import os
import socket
import time

def Scan():
    hostname = socket.gethostname()
    infoPack = socket.gethostbyname_ex(hostname)
    allIPs = infoPack[2]

    if len(allIPs) > 1:
        myIP = allIPs[1]
    else:
        myIP = allIPs[0]

    basIP = ".".join(myIP.split(".")[:-1]) + "."
    print(f"\nDetected network: {basIP}")

    zabraneIP = []
    for i in range(1, 256):
        targetIP = basIP + str(i)
    
        response = os.system(f"ping -n 1 -w 100 {targetIP} > nul")
        time.sleep(0.5)

        if response == 0:
            try:
                name = socket.gethostbyaddr(targetIP)[0]
                print(f"IP {targetIP} is ACTIVE - {name}")
                zabraneIP.append(targetIP)
            except socket.herror:
                print(f"IP {targetIP} is ACTIVE - Name: Unknown")
                zabraneIP.append(targetIP)
        else:
            print(f"Checking: {targetIP}", end="\r")

    print()
    print(f"\n{len(zabraneIP)} WAS FOUND:")
    print(f"List of active IPs: {', '.join(zabraneIP)}")