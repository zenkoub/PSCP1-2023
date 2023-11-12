"""Math for IT"""
import math
def main():
    """Math for IT"""
    radiussize = float(input())
    area1 = (math.pi)*(radiussize**2)
    circum = 2*(math.pi)*radiussize
    print("Area:", "%.3f" % area1)
    print("Circumference:", "%.3f" % circum)
main()
