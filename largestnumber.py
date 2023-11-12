'''largestnumber'''
def find(num1, num2):
    """findthelargest"""
    if num1 > num2:
        return num1
    return num2
def main():
    """printthelargest"""
    numa = input()
    numb = input()
    numc = input()
    sumval = find(numa+numb+numc, numa+numc+numb)
    sumval = find(sumval, numb+numa+numc)
    sumval = find(sumval, numb+numc+numa)
    sumval = find(sumval, numc+numb+numa)
    sumval = find(sumval, numc+numa+numb)
    print(int(sumval))
main()
