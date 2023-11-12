'''compoundinterest'''
def main():
    '''printtheamountofmoneythatrecievedinNyear'''
    principle = int(input())
    rate = float(input())
    year = int(input())
    for _ in range(year):
        principle += principle * rate / 100
    print("%.2f" % principle)
main()
