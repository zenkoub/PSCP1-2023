'''pickthem'''
import json
def main():
    '''pickevennuminlist'''
    list_n = json.loads(input())
    list_n1 = []
    for num in list_n:
        if num % 2 == 0:
            list_n1.append(num)
    if list_n1 == []:
        print("Nope")
    for i in list_n1:
        print(i)
main()
