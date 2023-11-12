'''atm_recommend'''
def process(transaction, currentamount):
    '''process'''
    enum = transaction.split()
    if enum[0] == "D":
        currentamount += int(enum[1])
    elif enum[0] == "W":
        if currentamount >= int(enum[1]):
            currentamount -= int(enum[1])
        else:
            currentamount -= currentamount
    return currentamount

def main():
    '''printamount'''
    amount = 0
    amount = int(input())
    while True:
        transaction = input()
        if transaction == "END":
            break
        amount = process(transaction, amount)
    print(amount)

main()
