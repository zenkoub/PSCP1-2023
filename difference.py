'''difference'''
def main(set_a_num, set_b_num):
    '''printout A-B '''
    set_a = set()
    set_b = set()
    for _ in range(set_a_num):
        set_a_value = int(input())
        set_a.add(set_a_value)
    for _ in range(set_b_num):
        set_b_value = int(input())
        set_b.add(set_b_value)
    difference = set_a - set_b
    for i in sorted(difference):
        print(i, end=" ")
main(int(input()), int(input()))
