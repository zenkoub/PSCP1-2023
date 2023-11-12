'''total'''
def main():
    '''milk'''
    priceper = int(input())
    eachlid = int(input())
    trade = int(input())
    money = int(input())
    total = money // priceper
    var = total
    while var >= eachlid and trade != 0:
        if eachlid == 0:
            break
        total += trade
        var += trade
        var -= eachlid
    print(total)
main()
