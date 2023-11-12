'''tuple's sad life'''
def main():
    '''tuplefirstproblem'''
    num = input().replace(' ', "")
    value = input()
    indexnum = num.index(value)
    countnum = num.count(value)
    for _ in range(countnum):
        for _ in range(countnum):
            print(indexnum, end=" ")
        print()

main()
