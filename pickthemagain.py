'''pickagain'''
def main():
    '''printnumthatcanbedividedby 3 or 5'''
    text = input().split()
    mylist = []
    for i in text:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            mylist.append(int(i))
    if mylist == []:
        print("Nope")
    for i in mylist[: :-1]:
        print(i)
main()
