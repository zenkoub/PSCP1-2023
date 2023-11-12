'''validvar'''
def main():
    '''indicateifvalidornot'''
    numline = int(input())
    for _ in range(numline):
        message = input()
        if message.isidentifier() and (message != "if" \
        and message != "else" and message != "elif" and message != "for" \
        and message != "while" and message != "True" and message != "False" \
        and message != "continue" and message != "break" and message != "return" \
        and message != "is" and message != "in" and message != "and" \
        and message != "or" and message != "from" and message != "as" \
        and message != "pass" and message != "not" \
        and message != "def" and message != "None"):
            print("Valid")
        else:
            print("Invalid")
main()
