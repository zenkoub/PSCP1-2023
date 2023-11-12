"""surprisingvote"""
def main():
    """indicateifsurprisingornot"""
    sumofthree = float(input())
    highest = float(input())
    if abs(3*highest - sumofthree) > 2 and highest != 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
