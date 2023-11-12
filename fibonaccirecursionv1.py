'''fibonaccirecursionv1'''
def funcnum(num):
    '''fibonacci'''
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return funcnum(num-1) + funcnum(num-2)
def main():
    """printout"""
    print(funcnum(int(input())))
main()
