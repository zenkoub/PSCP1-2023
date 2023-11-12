'''lotto'''
def main():
    '''caltheprize'''
    first = input()
    lastdigit2 = input()
    frontdigit3_1 = input()
    frontdigit2 = input()
    lastdigit3_1 = input()
    lastdigit3_2 = input()
    mylotto = input()
    money = 0
    nearfront1 = ""
    nearfront2 = ""
    if first == "000000":
        nearfront1 = "000001"
        nearfront2 = "999999"
    elif first == "999999":
        nearfront1 = "999998"
        nearfront2 = "000000"
    else:
        nearfront1 = ("%06d" %(int(first)-1))
        nearfront2 = ("%06d" %(int(first)+1))
    if mylotto == first:
        money += 6000000
    if mylotto == nearfront1 or mylotto == nearfront2:
        money += 100000
    if mylotto[-2:] == lastdigit2:
        money += 2000
    if mylotto[:3] == frontdigit3_1:
        money += 4000
    if mylotto[:3] == frontdigit2:
        money += 4000
    if mylotto[-3:] == lastdigit3_1:
        money += 4000
    if mylotto[-3:] == lastdigit3_2:
        money += 4000
    print(money)
main()
