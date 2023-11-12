'''pro'''
def main(properson, propay, priceper, person):
    '''promotion'''
    freeperson = properson - propay
    freeround = person // properson
    totalprice = priceper * (person - (freeround*freeperson))
    print(totalprice)
main(int(input()), int(input()), int(input()), int(input()))
