'''ruleofthree'''
def main():
    '''printoutbestprice'''
    sizeavailble = int(input())
    price = float(input())
    size = float(input())
    acprice = size/price
    var_1 = acprice
    bestprice = price
    for _ in range(sizeavailble-1):
        price = float(input())
        size = float(input())
        acprice = size/price
        if acprice > var_1:
            bestprice = price
            var_1 = acprice
        elif acprice == var_1:
            if price < bestprice:
                bestprice = price
                var_1 = acprice
        else:
            bestprice = bestprice
            var_1 = var_1
    print("%.2f %.2f" %(bestprice, var_1*bestprice))
main()
