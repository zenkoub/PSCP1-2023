'''christmastree'''
def main(nval, kval):
    '''printout * as leaves and --- as logs'''
    for i in range(1, nval + 1):
        space = " " * (nval - i)
        leaves = "*" * (2 * i - 1)
        print(space + leaves)
    for i in range(kval):
        space = " " * (nval - 2)
        logs = "-" * 3
        print(space + logs)
main(int(input()), int(input()))
