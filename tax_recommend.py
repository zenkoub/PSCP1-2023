'''recommend'''
def main():
    '''tax'''
    year = int(input())
    size = int(input())
    tax = 0
    if size > 1800:
        tax += (size-1800)*4
        size = 1800
    if size > 600:
        tax += (size-600)*1.5
        size = 600
    tax += size*0.5

    if year == 6:
        tax = tax*(90/100)
    elif year == 7:
        tax = tax*(80/100)
    elif year == 8:
        tax = tax*(70/100)
    elif year == 9:
        tax = tax*(60/100)
    elif year >= 10:
        tax = tax*(50/100)
    print("%.2f" % (tax))

main()
