'''sequencexxx'''
def main():
    '''printoutsequenceasXpattern'''
    num1 = int(input())
    num2 = int(input())
    for i in range(num1):
        if i == 0 or i == num1-1:
            for _ in range(num2):
                print("*"*num1, end=" ")
            print()
        else:
            for _ in range(num2):
                for j in range(num1):
                    if i == j or j == 0 or j == num1-1 or j == num1-1-i:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print("", end=" ")
            print()
main()
