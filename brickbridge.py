"""brickbridge"""
def main():
    """brickbridge"""
    small = abs(int(input()))
    big = abs(int(input()))
    goal = abs(int(input()))
    if (big*5) + small < goal or big%5 > small:
        print(-1)
    else:
        if big*5 >= goal:
            print(goal%5)
        else:
            print(goal-(big*5))
main()
