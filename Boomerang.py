"""Boomerang"""
def main():
    """Boomerang"""
    from math import sqrt
    var1 = int(input())
    var2 = int(input())
    var3 = int(input())
    func1 = var1 + 1
    func2 = 7*var2**3 + 2*var2**2 - 31*var2 + 1
    func3 = -(var3)
    func4 = (var1 + var2)*(var1 - var2)
    rooted = sqrt(var2**2-4*var1*var3)
    func5 = ((var2 - rooted)/(2*var1))
    print(func1)
    print(func2)
    print(func3)
    print(func4)
    print(func5)
main()
