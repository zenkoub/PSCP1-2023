"""CircularI"""
def main():
    """indicateoutputbetweentwopoints"""
    xme = float(input())
    yme = float(input())
    radius = float(input())
    xmos = float(input())
    ymos = float(input())
    circle = (((xme-xmos)**2)+((yme-ymos)**2))**0.5
    if circle <= radius:
        print("Yes")
    else:
        print("No")
main()
