'''matrix_MN'''
def main():
    '''printoutthenuminmatrix3x3'''
    size_m = int(input())
    size_n = int(input())
    space = ""
    for _ in range(size_m):
        for _ in range(size_n):
            space += input()+" "
        print(space)
        space = ""
main()
