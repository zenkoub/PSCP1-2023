'''blackjack'''
def main():
    '''sumofblackjack'''
    num = int(input())
    point = 0
    var = 0
    for i in range(num):
        i = i
        card = input()
        if card in "JQKjqk":
            point += 10
        elif card in "Aa":
            var += 1
        else:
            point += int(card)
    while var > 0:
        var -= 1
        if point + 11 > 21:
            point += 1
        elif point == 10 and var == 1:
            point += 1
        else:
            point += 11
    print(point)
main()
