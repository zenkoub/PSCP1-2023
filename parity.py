'''parity'''
def main():
    """Parity"""
    bina = input()
    typ = input()
    binachange = bina.replace("0", "")
    if typ == "Even":
        if len(binachange) % 2 == 0:
            print(bina+"0")
        else:
            print(bina+"1")
    elif typ == "Odd":
        if len(binachange) % 2 == 0:
            print(bina+"1")
        else:
            print(bina+"0")
main()
