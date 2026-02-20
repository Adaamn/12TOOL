#  ____      _     ____   ____  __        __  ___   ____   ____      ____  _____  _   _ 
# |  _ \    / \   / ___| / ___| \ \      / / / _ \ |  _ \ |  _ \    / ___|| ____|| \ | |
# | |_) |  / _ \  \___ \ \___ \  \ \ /\ / / | | | || |_) || | | |  | |  _ |  _|  |  \| |
# |  __/  / ___ \  ___) | ___) |  \ V  V /  | |_| ||  _ < | |_| |  | |_| || |___ | |\  |
# |_|    /_/   \_\|____/ |____/    \_/\_/    \___/ |_| \_\|____/    \____||_____||_| \_|

import random

words = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special = ["@", "#", "$", "%", "^", "&", "*", "(", ")", "!", "?", "_", "-", "+", "=", "[", "]", "{", "}", "<", ">", "/", "|", "\\", "~", ":", ";", ".", ","]

symbols = list(words+numbers)+special

def genPass(passLength):
    if passLength > 0:
        if passLength <= 100:
            fpassword = []
            for i in range(passLength):
                randSymb = random.choice(symbols)
                fpassword.append(randSymb)
            print ("Generated password:","".join(fpassword))
        else:
            print("Only 100 symbols allowed.")
    else:
        print("More than 0 symbols required.")