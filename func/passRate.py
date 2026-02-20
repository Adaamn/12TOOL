""" #  ____      _     ____   ____  __        __  ___   ____   ____     ____      _     _____  _____ 
# |  _ \    / \   / ___| / ___| \ \      / / / _ \ |  _ \ |  _ \   |  _ \    / \   |_   _|| ____|
# | |_) |  / _ \  \___ \ \___ \  \ \ /\ / / | | | || |_) || | | |  | |_) |  / _ \    | |  |  _|  
# |  __/  / ___ \  ___) | ___) |  \ V  V /  | |_| ||  _ < | |_| |  |  _ <  / ___ \   | |  | |___ 
# |_|    /_/   \_\|____/ |____/    \_/\_/    \___/ |_| \_\|____/   |_| \_\/_/   \_\  |_|  |_____|

specials = ["@", "#", "$", "%", "^", "&", "*", "(", ")", "!", "?", "_", "-", "+", "=", "[", "]", "{", "}", "<", ">", "/", "|", "\\", "~", ":", ";", ".", ","]

def ratePass(password):

    special = False
    upper = False
    num = False

    if len(password) <= 8:
        print("Your password is too short.")
        return
    
    for char in password:
        if char in specials:
            special = True
        if char.isupper():
            upper = True
        if char.isdigit():
            num = True

    if special == True and upper == True and num == True:
        return print("Your password contains all of the safety criteria, its safe.") 
    else:
        what = []
        if not special:
            what.append("special character")
        if not upper:
            what.append("upper symbol")
        if not num:
            what.append("number")
        return print("Your password is not safe, missing:",", ".join(what) ) """