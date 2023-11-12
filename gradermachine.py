"""gradermachine"""
def main():
    """superviseweightandcalthesum"""
    passval = ""
    sumval = 0
    start = int(input())
    stop = int(input())
    if start >= stop:
        for i in range(start, stop-1, -1):
            if i % 2 == 0:
                passval += str(i)+" "
                sumval += i
    else:
        for i in range(start, stop+1):
            if i % 2 == 0:
                passval += str(i)+" "
                sumval += i
    print("pass : %s" % passval)
    print("Sum : %d" % sumval)
main()
