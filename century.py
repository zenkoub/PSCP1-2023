'''century'''
import math
def main():
    """Century"""
    num = int(input())
    for _ in range(num):
        yearstr = " "
        yeartype = input()
        for check in yeartype:
            if check.isdigit():
                yearstr += check
        yearint = int(yearstr)
        if "B.E." in yeartype.upper():
            yearint -= 543
        elif "A.D." in yeartype.upper():
            yearint = yearint
        else:
            print("ERROR")
            break
        if yearint <= 0:
            print("ERROR")
        else:
            century = math.ceil(yearint/100)
            print(century)
main()
