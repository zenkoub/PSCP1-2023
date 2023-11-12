'''for!fball'''
def main():
    '''print out 1 or 2 or 3'''
    text = input()
    spot = 1
    for i in text:
        if i == "A":
            if spot == 1:
                spot = 2
            elif spot == 2:
                spot = 1
        elif i == "B":
            if spot == 2:
                spot = 3
            elif spot == 3:
                spot = 2
        elif i == "C":
            if spot == 1:
                spot = 3
            elif spot == 3:
                spot = 1
    print(spot)
main()
