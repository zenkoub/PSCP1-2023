"""DataSpike"""
def main():
    """printthemostvalue"""
    most = 0
    most = mostnum(int(input()), most)
    most = mostnum(int(input()), most)
    most = mostnum(int(input()), most)
    most = mostnum(int(input()), most)
    most = mostnum(int(input()), most)
    most = mostnum(int(input()), most)
    most = mostnum(int(input()), most)
    most = mostnum(int(input()), most)
    print(most)
def mostnum(num, most):
    """pickthemostnumber"""
    if num > most:
        most = num
    return most
main()
