from func import getPrice, genPass, ratePass

print(" __  __  _____  _   _  _   _ ")
print("|  \/  || ____|| \ | || | | |")
print("| |\/| ||  _|  |  \| || | | |")
print("| |  | || |___ | |\  || |_| |")
print("|_|  |_||_____||_| \_| \___/ ")
print("")

print("[1] - Password Generator")
print("[2] - Password Rate")
print("[3] - Cryptocurrency price")
print("[4] - Exit")
print("")

def intLoad(text):
    while True:
        try:
            num = int(input(text))
            break
        except ValueError: print("Numbers only.")
    return num

while True:
    choice = intLoad("\nEnter your choice: ")

    if choice == 1:
        passlength = intLoad("\nHow many symbols: ")
        print(f"Generated password: {genPass(passlength)}")

    elif choice == 2:
        typePass = input("\nEnter the password you want to rate: ")
        ratePass(typePass)

    elif choice == 3:
        crypto = input("\nType a cryptocurrency: ").strip().lower()
        usd, eur, czk, cryptoName = getPrice(crypto)
        if usd != None:
            print(f"\n--- Current price of {cryptoName}: ---")
            print(f"USD: {usd:,}")
            print(f"EUR: {eur:,}")
            print(f"CZK: {czk:,}")
    elif choice == 4:
        break