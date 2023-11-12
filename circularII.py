"""CircularII"""
def main():
    """comparebetweentworadiuses"""
    xme = float(input())
    yme = float(input())
    radiusme = float(input())
    xfriend = float(input())
    yfriend = float(input())
    radiusfriend = float(input())
    circle = (((xme-xfriend)**2)+((yme-yfriend)**2))**0.5
    if circle >= radiusme - radiusfriend:
        print("Yes")
    elif circle >= radiusfriend - radiusme:
        print("Yes")
    else:
        print("No")
main()
