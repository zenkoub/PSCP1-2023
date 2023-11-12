'''alexandria'''
def main(a_val, b_val, c_val):
    '''alexandria'''
    s_var = (a_val + b_val + c_val)/2
    area = (s_var*(s_var-a_val)*(s_var-b_val)*(s_var-c_val))**0.5
    print("%.3f" % area)
main(float(input()), float(input()), float(input()))
