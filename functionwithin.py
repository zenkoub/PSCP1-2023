"""function"""
def main():
    """fucnone"""
    val_1 = float(input())
    val_2 = float(input())
    val_3 = float(input())
    val_4 = float(input())
    print(float(((one(one(val_1))))))
    print(float((two(one(val_1-val_2)))))
    print(float((three((one(val_1+val_2)), (one(val_1+val_3)), two(one(val_4**2))))))
    print(float(four(three(one(val_1+val_2), one(val_1-val_3), two(one(val_4**2))), \
                     two(one(val_1-val_2)), one(one(one(one(one(val_3))))), val_4**8)))
def one(val):
    """calculatefuncone"""
    return 2*(val)
def two(val):
    """calthreefunctwo"""
    return 3*((val)**4)-((val)**3)+(2*(val**2))+10
def three(valx, valy, valz):
    """calthreefunc"""
    return ((valz+valx)**2)-(valx*valy)+(valy**2)
def four(vala, valb, valc, vald):
    """calfourfunc"""
    return ((vala**2)+(valb**2)-(valc**2))/((vald**2)-(2*vala*vald)+(2*vala))
main()
