'''bmi'''
def bmi():
    '''bmi'''
    name = input()
    weight = float(input())
    height = float(input())/100
    result = weight/(height**2)
    print(name + "'s" + " " + " " + "BMI" + " " + "=" + " " "%.2f" % result)
def main():
    '''printeachpersonbmi'''
    bmi()
    bmi()
    bmi()
    bmi()
    bmi()
main()
