"""EuclideanDistance2D"""
from math import sqrt
def main():
    """EuclideanDistance2D"""
    val_1 = float(input())
    val_2 = float(input())
    secval_1 = float(input())
    secval_2 = float(input())
    result = sqrt(((val_1-secval_1)**2) + ((val_2-secval_2)**2))
    print(result)
main()
