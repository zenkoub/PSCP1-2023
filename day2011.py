'''day2011'''
def main(day, month):
    '''findwhichday'''
    for i in range(1, month):
        if i == 3 or i == 5 or i == 7 \
        or i == 8 or i == 10 or i == 12:
            day += 31
        elif i == 2:
            day += 28
        elif i == 1 and month > 1:
            day += 31
        elif i == 4 or 6 or 9 or 11:
            day += 30
    if day % 7 == 0:
        print("Friday")
    elif day % 7 == 1:
        print("Saturday")
    elif day % 7 == 2:
        print("Sunday")
    elif day % 7 == 3:
        print("Monday")
    elif day % 7 == 4:
        print("Tuesday")
    elif day % 7 == 5:
        print("Wednesday")
    elif day % 7 == 6:
        print("Thursday")
main(int(input()), int(input()))
