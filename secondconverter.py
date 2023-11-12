'''secondconverter'''
def main():
    '''convert to hour:minute:second format'''
    k_val = int(input())
    second = int(input())
    minute = int(input())
    hour = int(input())
    actualseond = k_val % second
    actualminute = k_val // second
    actualhour = actualminute // minute
    actualminute = actualminute % minute
    actualhour = actualhour % hour
    if actualhour > hour:
        actualhour = actualhour % hour
    print("%d:%d:%d" % (actualhour, actualminute, actualseond))
main()
