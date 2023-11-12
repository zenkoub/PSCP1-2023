"""rata"""
def main():
    """rata"""
    message = input()
    text = message.upper()
    count = 0
    while count > len(text):
        if text == "6" or "7" or "Y" or "U" or "H" or "J" or "N" or "M":
            count = count + 1
        print(count)
main()
