#  ____      _     ____   ____  __        __  ___   ____   ____      ____  _____  _   _ 
# |  _ \    / \   / ___| / ___| \ \      / / / _ \ |  _ \ |  _ \    / ___|| ____|| \ | |
# | |_) |  / _ \  \___ \ \___ \  \ \ /\ / / | | | || |_) || | | |  | |  _ |  _|  |  \| |
# |  __/  / ___ \  ___) | ___) |  \ V  V /  | |_| ||  _ < | |_| |  | |_| || |___ | |\  |
# |_|    /_/   \_\|____/ |____/    \_/\_/    \___/ |_| \_\|____/    \____||_____||_| \_|

import random, string

symbols = string.ascii_letters+string.punctuation+string.digits

def genPass(passLength):
    if passLength >= 3:
        if passLength <= 100:
            fpassword = []
            for i in range(passLength):
                randSymb = random.choice(symbols)
                fpassword.append(randSymb)
            print ("Generated password:","".join(fpassword))
        else:
            print("Only 100 symbols allowed.")
    else:
        print("At least 3 symbols required.")