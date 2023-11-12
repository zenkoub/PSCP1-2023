'''recommmend'''
def main():
    '''pongya'''
    num = int(input())
    num_last = num % 10
    if num % 3 == 0 or num_last == 3:
        print("PONG")
    else:
        print(num)
main()
