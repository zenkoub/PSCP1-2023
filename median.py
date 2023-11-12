'''median'''
def main():
    '''printthemedianofthesenumbers'''
    num = int(input())
    list_n = []
    for _ in range(num):
        numbers = int(input())
        list_n.append(numbers)
        list_n.sort()
    if num % 2 == 0:
        median1 = list_n[num//2 -1]
        median2 = list_n[num//2]
        median = (median1 + median2)/2
    else:
        median = list_n[num//2]
    print("%.1f" % median)

main()
