'''linesorting'''
def main():
    '''printfromshortesttolongest'''
    num = int(input())
    list_n = []
    for i in range(num):
        text = input()
        list_n.append(text)
        list_n.sort(key=len)
    for i in range(0, len(list_n)):
        print(list_n[i])

main()
