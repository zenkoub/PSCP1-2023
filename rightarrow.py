'''rightarrow'''
def main():
    '''printsequence'''
    width = int(input())
    height = int(input())
    middle = height//2
    for i in range(height):
        if i == 0 or i == height-1:
            print("*"*width)
        elif i > height//2:
            print(" "*(middle-1)+"*"*width)
            middle -= 1
        else:
            print(" "*(i)+"*"*width)
main()
