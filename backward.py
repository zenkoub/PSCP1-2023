'''backward'''
def main():
    '''printbackwards'''
    count = 100
    list_n = []
    for _ in range(count):
        text = input()
        list_n.append(text)
        if text == "NULL":
            break
    list_n.reverse()
    list_n.remove("NULL")
    for i in range(0, len(list_n)):
        print(list_n[i])
main()
