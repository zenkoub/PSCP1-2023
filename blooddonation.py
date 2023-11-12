'''blooddonation'''
def main():
    '''ejudge'''
    age = int(input())
    weight = int(input())
    num = int(input())
    ans = False
    certi = False
    if age == 17 or 60 <= age <= 70:
        certi = input()
    if (age == 17 or 60 <= age <= 70) and certi == 'False':
        ans = False
    elif (num == 0 and age > 55) or age < 17 or age > 70 or weight < 45:
        ans = False
    elif (age == 17 or 60 <= age <= 70) and certi == "True" and weight >= 45:
        ans = True
    elif 17 < age < 60 and weight >= 45:
        ans = True
    if ans:
        print("Yes")
    else:
        print("No")

main()
