'''roman'''
def main():
    '''convertsymboltobase10number'''
    symbol = str(input())
    total = 0
    for i in symbol:
        if i == "M":
            total += 1000
        if i == "D":
            total += 500
        if i == "C":
            total += 100
        if i == "L":
            total += 50
        if i == "X":
            total += 10
        if i == "V":
            total += 5
        if i == "I":
            total += 1
    print(total)

main()
