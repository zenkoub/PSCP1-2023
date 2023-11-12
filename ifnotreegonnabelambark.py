"""notree"""
def main():
    """notree"""
    fish = str(input())
    sailnum = float(input())
    fishh = fish.count("<^))))><")
    if fishh > sailnum and fishh > 0:
        print("We have many fish ahoyy!!!")
    elif fishh == sailnum and fishh > 0:
        print("We have enough fish for everyone.")
    elif fishh % sailnum != 0 or fishh < sailnum or fishh == 0:
        print("No one will eat them because the fish cannot be divided.")
    elif fishh % sailnum == 0 and fishh < sailnum and fishh > 0:
        print("We can share the fish together Yahoooo!!!")
    else:
        print("", end="")
main()
