'''isprimesmall'''
def main():
    '''primenumberchecker'''
    num = int(input())
    if num == 1:
        print("No")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("No")
                break
        else:
            print("Yes")
main()
