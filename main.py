import os
from func import getPrice, genPass, Scan

os.system('color c')

def intLoad(text):
    while True:
        try:
            num = int(input(text))
            break
        except ValueError: print("Numbers Only.")
    return num

while True:
    print(" __  __  _____  _   _  _   _ ")
    print("|  \/  || ____|| \ | || | | |")
    print("| |\/| ||  _|  |  \| || | | |")
    print("| |  | || |___ | |\  || |_| |")
    print("|_|  |_||_____||_| \_| \___/ ")
    print("")

    print("[1] - Password Generator")
    print("[2] - Cryptocurrency price")
    print("[3] - IPScan")
    print("[4] - Exit")
    print("")

    choice = intLoad("\nEnter your choice: ")

    if choice == 1:
        passlength = intLoad("\nHow many symbols: ")
        genPass(passlength)
        input("\nClick enter to continue..")
        os.system('cls')

    elif choice == 2:
        crypto = input("\nType a cryptocurrency: ").strip().lower()
        usd, eur, czk, cryptoName = getPrice(crypto)
        if usd != None:
            print(f"\n--- Current price of {cryptoName}: ---")
            print(f"USD: {usd:,}")
            print(f"EUR: {eur:,}")
            print(f"CZK: {czk:,}")
        input("\nClick enter to continue..")
        os.system('cls')
    
    elif choice == 3:
        Scan()
        input("\nClick enter to continue..")
        os.system('cls')

    elif choice == 4:
        break

    else:
        os.system('cls')