"""3d"""
def main():
    """3d"""
    var_x1 = float(input())
    var_y1 = float(input())
    var_z1 = float(input())
    var_x2 = float(input())
    var_y2 = float(input())
    var_z2 = float(input())
    result = ((var_x2-var_x1)**2)+((var_y2-var_y1)**2)+(var_z2-var_z1)**2
    print("%.2f" %(result)**0.5)
main()
