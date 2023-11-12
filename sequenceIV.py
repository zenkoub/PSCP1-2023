"""sequenceIV"""
def main():
    """printsequenceaspatterned"""
    num = int(input())
    currentnum = 1
    for _ in range(num):
        for _ in range(num):
            print(currentnum, end=" ")
            currentnum += 1
        print()
main()
