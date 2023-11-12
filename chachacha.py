'''chachacha'''
import math
def main():
    """Cha Cha Cha"""
    money = 0
    daywork = int(input())
    for _ in range(daywork):
        workhour = math.ceil(float(input()))
        money += workhour*8720
    print(money)
main()
