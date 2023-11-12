'''restaurant'''
def main():
    '''decideifyesorno and amount'''
    ordered = float(input())
    dueamount = float(input())
    discount = (100-float(input()))/100
    recommend = float(input())
    actualprice = ordered + recommend
    if actualprice >= dueamount:
        actualprice = actualprice*discount
    if ordered >= dueamount:
        ordered = ordered*discount
    if ordered < actualprice:
        print("No %.3f" % (actualprice-ordered))
    elif ordered > actualprice:
        print("Yes %.3f" % (ordered-actualprice))
    else:
        print("Yes")
main()
