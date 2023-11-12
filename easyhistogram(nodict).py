'''easyhistogram(nodict)'''
def main():
    '''printoutcountofeachindex'''
    text = input().replace(' ', '')
    list_n = []
    list_n.extend(text)
    list_n.sort(key=str.lower)
    for i in list_n:
        print(i, "=", list_n.count(i))

main()
