'''ascend'''
def main():
    '''printfrom lowest to highest'''
    list_n = []
    for _ in range(5):
        num = int(input())
        list_n.append(num)
        list_n.sort()
    for i in range(0, len(list_n)):
        print(list_n[i])
main()
