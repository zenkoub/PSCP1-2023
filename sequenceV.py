'''sequenceV'''
def main():
    '''printoutbackwards'''
    num = int(input())
    while num > 0:
        for _ in range(7):
            if num > 0:
                print(num, end=" ")
                num -= 1
        print()
main()
