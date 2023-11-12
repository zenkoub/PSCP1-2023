'''key'''
def main():
    '''printoutcalculatedvalue'''
    num = input()
    sumall = 0
    for i in range(len(num)):
        sumall += int(num[i])
    sumallnew = int(num[-3:])*10
    sumtotal = sumall + sumallnew
    if sumtotal < 1000:
        sumtotal += 1000
    print(str(sumtotal)[-4:])
main()
