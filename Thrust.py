"""Thrust"""
earth = 5.972*10**24
mars = 6.39*10**23
jupiter = 1.898*10**27
def main():
    """Thrust"""
    planet = input()
    distance = float(input())
    earth = (planet == "earth")*((5.972*10**24)*distance/10000)
    mars = (planet == "mars")*((6.39*10**23)*distance/10000)
    jupiter = (planet == "jupiter")*((1.898*10**27)*distance/10000)
    print(earth or mars or jupiter)
main()
