#   ____  ____  __   __ ____   _____   ___     ____   ____   ___   ____  _____ 
#  / ___||  _ \ \ \ / /|  _ \ |_   _| / _ \   |  _ \ |  _ \ |_ _| / ___|| ____|
# | |    | |_) | \ V / | |_) |  | |  | | | |  | |_) || |_) | | | | |    |  _|  
# | |___ |  _ <   | |  |  __/   | |  | |_| |  |  __/ |  _ <  | | | |___ | |___ 
#  \____||_| \_\  |_|  |_|      |_|   \___/   |_|    |_| \_\|___| \____||_____|

import requests

def getPrice(cryptoName):
    
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={cryptoName}&vs_currencies=usd,eur,czk"
    
    try:
        response = requests.get(url)

        if response.status_code == 429:
            print("[API] Too many requests")
            return None, None, None, cryptoName
        else:
            data = response.json()
            if cryptoName in data:
                usd = data[cryptoName]["usd"]
                eur = data[cryptoName]["eur"]
                czk = data[cryptoName]["czk"]
                return usd, eur, czk, cryptoName
            else:
                print("Cryptocurrency not found.")
                return None, None, None, cryptoName
    except Exception as e:
        print(f"There was an error - {e}")
        return None, None, None, cryptoName