'''robot'''
def main():
    '''robot'''
    name_1 = str(input())
    age_1 = float(input())
    if age_1 >= 18:
        print(name_1 + ", you shall not pass.")
    elif 0 < age_1 < 18:
        print(name_1 + ", you can pass.")
main()
