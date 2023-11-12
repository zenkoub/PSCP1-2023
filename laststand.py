'''laststand'''
def main():
    '''printthelastdigitofeachnumber'''
    list_n = input().strip("[]").split(",")
    for i in list_n:
        print(i[-1])
main()
