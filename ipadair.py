'''ipadair'''
def ipad(color, storage, connect):
    '''printouttheprice'''
    listcolor = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    if color in listcolor:
        if storage == 64:
            print(sixtyfour(storage, connect))
        elif storage == 256:
            print(twofivesix(storage, connect))
        else:
            print("Not Available")
    else:
        print("Not Available")

def sixtyfour(storage, connect):
    '''64'''
    if storage == 64:
        if connect == "Wi-Fi":
            return "19900"
        elif connect == "Wi-Fi + Cellular":
            return "24400"
        else:
            return "Not Available"

def twofivesix(storage, connect):
    '''256'''
    if storage == 256:
        if connect == "Wi-Fi":
            return "24900"
        elif connect == "Wi-Fi + Cellular":
            return "29400"
        else:
            return "Not Available"

ipad(input(), int(input()), input())