"""ascii"""
def main():
    """ascii"""
    message = input()
    double_1 = message.find('"')
    double_2 = message.rfind('"')
    if double_1 != -1 and double_2 != -1:
        numb = int(message[double_1+1:double_2])
        print(message[0:double_1] + chr(numb) + message[double_2+1:len(message)])
    else:
        print("No error")
main()
