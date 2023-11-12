'''Align'''
def main():
    '''align'''
    size = int(input())
    direction = str(input())
    message = str(input())
    if size == 30 and direction == "left":
        print(message+" "*(30-len(message)))
    elif size == 20 and direction == "center":
        space1 = (20-len(message))//2
        space2 = (20-len(message))%2
        print(" "*(space1+space2)+message+" "*space1)
    elif size == 40 and direction == "right":
        print(" "*(40-len(message))+message)
main()
