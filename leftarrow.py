'''leftarrow'''
def main(kval, nval):
    '''printoutarrowsymbolheadtotheleft'''
    for i in range(nval):
        if i < nval // 2:
            space = " " * (nval // 2 - i)
        else:
            space = " " * (i - nval // 2)
        asterisk = "*" * kval
        print(space + asterisk)
main(int(input()), int(input()))
