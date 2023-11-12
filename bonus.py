'''bonus'''
def main():
    '''bonus'''
    salary = int(input())
    year = int(input())
    month = int(input())
    if month == 10 or month == 11:
        year += 1
    bonus = year*salary
    if year > 20:
        bonus = 20*salary
    if bonus < 5000:
        bonus = 5000
    if bonus > 1000000:
        bonus = 1000000
    print(bonus)
main()
