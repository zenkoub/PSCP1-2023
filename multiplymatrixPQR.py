'''multiplymatrixPQR'''
def add(num1, num2, num3):
    '''add'''
    for _ in range(num1):
        list_n = []
        for _ in range(num2):
            few = int(input())
            list_n.append(few)
        num3.append(list_n)
    return num3

def main():
    '''main'''
    num1, num2, num3 = int(input()), int(input()), int(input())
    list_a = add(num1, num2, [])
    list_b = add(num2, num3, [])
    for i in list_a:
        for j in range(len(list_b[0])):
            sum_n, count = 0, 0
            for k in i:
                sum_n += k * int(list_b[count][j])
                count += 1
            print(sum_n, end=" ")
        print()
main()
