'''inverter'''
def main():
    '''invert 0's and 1's'''
    num = input()
    ans = ""
    for i in num:
        if i == "0":
            ans += "1"
        elif i == "1":
            ans += "0"
    for i in range(len(ans)):
        if ans[i] == "1":
            print(ans[i:])
            break
main()
