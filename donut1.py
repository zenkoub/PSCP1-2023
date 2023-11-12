"""Donut"""
def main():
    """findthepriceandnumofdonuts"""
    priceper = int(input())
    piece = int(input())
    addon = int(input())
    desired = int(input())
    donut = 0
    purchase = piece+addon
    acdonut = desired // purchase
    if desired == 0:
        print("0 0")
    if desired > 0:
        donut = purchase * acdonut
        left = desired - donut
        if left > piece:
            left = piece
        if left >= piece:
            donut += purchase
        else:
            donut += left
        print("%d %d" %((priceper*acdonut*piece)+(left*priceper), donut))
main()
