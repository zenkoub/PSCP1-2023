'''area'''
def main():
    '''recommend'''
    lines = int(input())
    count = ""
    for _ in range(lines):
        area = input().replace(" ", "")
        count += area
    print(len(count))

main()
