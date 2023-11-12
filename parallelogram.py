'''parallelogram'''
def main():
    '''printfrombacktofrontaspatterned'''
    message = input()
    for i in range(len(message)):
        for j in range(i+1, len(message)):
            print(" ", end="")
        for j in range(0, i+1):
            print(message[j], end="")
        print()
    for i in range(len(message)-1):
        print(message[i+1:len(message)])
    print()
main()
