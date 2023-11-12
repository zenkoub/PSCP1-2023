'''runlengthdecoding'''
def main():
    '''decodeabbreviatedtofull'''
    message = input()
    decode = ""
    for i in message:
        if i.isdigit():
            decode += i
        else:
            print(i * int(decode), end="")
            decode = ""
main()
