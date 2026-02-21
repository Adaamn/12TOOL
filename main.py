import os
from func import getPrice, genPass, Scan, pubIPCheck

is_windows = os.name == 'nt'
if is_windows:
    os.system('color c')

def intLoad(text):
    while True:
        try:
            num = int(input(text))
            break
        except ValueError: print("Numbers Only.")
    return num

while True:
    if is_windows:
        os.system('cls')
    else:
        os.system('clear')

    print(" _  ____   _____   ___    ___   _     ")
    print("/ ||___ \ |_   _| / _ \  / _ \ | |    ")
    print("| |  __) |  | |  | | | || | | || |    ")
    print("| | / __/   | |  | |_| || |_| || |___ ")
    print("|_||_____|  |_|   \___/  \___/ |_____|")
    print("")

    print("[1] - Password Generator")
    print("[2] - Cryptocurrency Price")
    print("[3] - Local IP Scan")
    print("[4] - Public IP Scan")
    print("[5] - Exit")
    print("")

    choice = intLoad("Enter your choice: ")

    if choice == 1:
        passlength = intLoad("\nHow many symbols: ")
        genPass(passlength)
        input("\nClick enter to continue..")

    elif choice == 2:
        crypto = input("\nType a cryptocurrency: ").strip().lower()
        usd, eur, czk, cryptoName = getPrice(crypto)
        if usd != None:
            print(f"\n--- Current price of {cryptoName}: ---")
            print(f"USD: {usd:,}")
            print(f"EUR: {eur:,}")
            print(f"CZK: {czk:,}")
        input("\nClick enter to continue..")
    
    elif choice == 3:
        Scan()
        input("\nClick enter to continue..")

    elif choice == 4:
        pubIPCheck()
        input("\nClick enter to continue..")

    elif choice == 5:
        break