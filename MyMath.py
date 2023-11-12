"""math"""
import math
def main():
    """math"""
    degtorad = math.pi / 180
    num1 = math.sin(90 * degtorad)
    num2 = math.sin(60 * degtorad)**2
    num3 = math.cos((245**2) * degtorad)
    num4 = math.cos((45+135) * degtorad)
    print((num1 + num2)/(num3 + num4))
    print((math.factorial(16)*math.factorial(4))/(math.factorial(8)))
    print((15+25)/(math.sqrt((25-12)**2 + (12-15)**2)))
    print(math.log(1234**4, 10))
    print(((math.log(4234, 5)) + (math.log(8191, 2))+ (71*(math.log(156154, 10))))/
          ((math.log(777, 7))-(math.log(888, 8))-(math.log(999, 9))))
main()
