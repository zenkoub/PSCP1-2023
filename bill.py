'''bill'''
def main():
    '''printoutthevatandfeeincludedprice'''
    foodprice = int(input())
    servicecharge = 0.1*foodprice
    if servicecharge <= 50:
        vat = (foodprice+50)*0.07 # vat consists 7% of 'foodprice and 50 fees included'
        actualprice = 50+vat+foodprice # must plus the minimum servicecharge
    elif servicecharge >= 1000:
        vat = (foodprice+1000)*0.07 # same according to the above
        actualprice = 1000+vat+foodprice # must plus the maximum servicecharge
    else:
        vat = (foodprice+servicecharge)*0.07
        actualprice = vat+servicecharge+foodprice
    print("%.2f" % actualprice)
main()
