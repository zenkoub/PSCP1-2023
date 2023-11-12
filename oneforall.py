'''oneforall'''
def main():
    '''printorder'''
    gen = int(input())
    order = ""
    for i in range(1, gen+1):
        if i == gen:
            order += input()+"_"+str(i)
        elif i % 2 == 0:
            order += input()+"-"*i
        elif i % 2 == 1:
            order += input()+"*"*i
    print(order)
main()
