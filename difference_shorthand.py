'''difference'''
def main(set_a_num, set_b_num):
    """Difference"""
    set_a = {int(input()) for i in range(set_a_num)}
    set_b = {int(input()) for i in range(set_b_num)}
    difference = set_a - set_b
    for i in sorted(difference):
        print(i, end=' ')
main(int(input()), int(input()))
