'''sequenceVIII'''
def main():
    '''printoutsequencewith 0's'''
    num = int(input())
    space = 3*num - 3
    for i in range(1, num+1):
        for j in range(space):
            print(end=" ")
        space = space -3
        for j in range(1, i+1):
            print("%.02d" % j, end=" ")
        print("\r")
main()
