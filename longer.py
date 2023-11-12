'''midterm2023 longer'''
import math
def main(val_r, val_a, val_b):
    '''longer'''
    circle = 2*(math.pi)*val_r
    rectangle = (2*val_a)+(2*val_b)
    subtraction = abs(circle-rectangle)
    if circle > rectangle:
        print("Circle is longer")
        print("%.5f" % float(subtraction))
    elif circle < rectangle:
        print("Rectangle is longer")
        print("%.5f" % float(subtraction))
    else:
        print("Equal")
        print("%.5f" % float(subtraction))
main(float(input()), float(input()), float(input()))
