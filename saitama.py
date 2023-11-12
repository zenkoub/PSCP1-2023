'''saitama'''
import math
def main():
    """saitama"""
    pushupwant = int(input())
    situpwant = int(input())
    squatwant = int(input())
    runwant = int(input())
    pushupday = int(input())
    situpday = int(input())
    runday = int(input())
    squatday = int(input())
    pushup = pushupwant/pushupday
    situp = situpwant/situpday
    run = runwant/runday
    squat = squatwant/squatday
    if pushup > situp:
        var1 = pushup
    else:
        var1 = situp
    if squat > run:
        var2 = squat
    else:
        var2 = run
    if var1 > var2:
        print(math.ceil(var1))
    else:
        print(math.ceil(var2))
main()
