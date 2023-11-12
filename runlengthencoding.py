'''runlengthencoding'''
def main():
    '''printoutthenumberofeachalphabets'''
    message = input()
    countper = message[0]
    numper = 0
    acstring = ""
    for i in range(len(message)):
        if message[i] == countper:
            numper += 1
        else:
            acstring += str(numper) + message[i-1]
            countper = message[i]
            numper = 1
    acstring += str(numper) + message[-1]
    print(acstring)
main()
