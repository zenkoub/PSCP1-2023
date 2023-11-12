'''homerun'''
def main():
    '''printamountofhomeruns'''
    num = int(input())
    hit = float(input())
    homerun = 0
    for length in range(num):
        length = float(input())
        if length < hit:
            homerun += 1
    print(homerun)
main()
