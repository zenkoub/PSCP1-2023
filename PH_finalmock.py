'''finalmock'''
def main(num):
    '''PH'''
    if num >= 0 and num < 7:
        print("acidic")
    elif num == 7:
        print("neutral")
    elif num > 7 and num <= 14:
        print("akaline")
    elif num < 0 or num > 14:
        print("error")

main(float(input()))
