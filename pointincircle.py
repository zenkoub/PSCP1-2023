'''mathcircle'''
def main():
    '''decideifinthecirornot'''
    x_val = float(input())
    y_val = float(input())
    radius = float(input())
    xn_val = float(input())
    yn_val = float(input())
    total = ((xn_val-x_val)**2+(yn_val-y_val)**2)**0.5
    radiussqr = radius**2
    if total**2 <= radiussqr:
        print("True")
    else:
        print("False")
main()
