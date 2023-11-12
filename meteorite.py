'''meteorite'''
def main():
    '''printint'''
    weight = float(input())
    amounteach = int(input())
    safezone = float(input())
    meteorite = 1
    rocket = 0
    while weight >= safezone:
        rocket += meteorite
        meteorite = amounteach*meteorite
        weight /= amounteach
    print(rocket)
main()
