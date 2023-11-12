'''phonenum'''
def main():
    '''indicatethetypeandprintoutthedesriedformat'''
    number = input()
    connection = str(input())
    if connection == "Domestic":
        if len(number) == 9:
            print(number[0], number[1:5], number[5:9])
        elif len(number) == 10:
            print(number[0:2], number[2:6], number[6:10])
    elif connection == "International":
        if len(number) == 9:
            print("+66", number[1:5], number[5:9])
        elif len(number) == 10:
            print("+66"+number[1], number[2:6], number[6:10])
main()
