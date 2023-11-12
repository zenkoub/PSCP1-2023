'''iphone13again'''
def main(model, storage):
    '''indicatetheprice'''
    if model == "iPhone 13 mini":
        print(mini(model, storage))
    elif model == "iPhone 13":
        print(regular(model, storage))
    elif model == "iPhone 13 Pro":
        print(pro(model, storage))
    elif model == "iPhone 13 Pro Max":
        print(promax(model, storage))
    else:
        print("Not Available")

def mini(model, storage):
    '''mini'''
    if model == "iPhone 13 mini":
        if storage == "128 GB":
            return "25900"
        elif storage == "256 GB":
            return "29900"
        elif storage == "512 GB":
            return "37900"
        else:
            return "Not Available"

def regular(model, storage):
    '''regular'''
    if model == "iPhone 13":
        if storage == "128 GB":
            return "29900"
        elif storage == "256 GB":
            return "33900"
        elif storage == "512 GB":
            return "41900"
        else:
            return "Not Available"

def pro(model, storage):
    '''pro'''
    if model == "iPhone 13 Pro":
        if storage == "128 GB":
            return "38900"
        elif storage == "256 GB":
            return "42900"
        elif storage == "512 GB":
            return "50900"
        elif storage == "1 TB":
            return "58900"
        else:
            return "Not Available"

def promax(model, storage):
    '''promax'''
    if model == "iPhone 13 Pro Max":
        if storage == "128 GB":
            return "42900"
        elif storage == "256 GB":
            return "46900"
        elif storage == "512 GB":
            return "54900"
        elif storage == "1 TB":
            return "62900"
        else:
            return "Not Available"

main(str(input()), str(input()))
