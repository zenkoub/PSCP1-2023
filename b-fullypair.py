'''b-fullypair'''
def main():
    """B - Fully pair?"""
    word = input().lower()
    var_1 = ""
    nopair = ""
    count = 0
    for app in word:
        if var_1.count(app) <= 0:
            var_1 += app
    for app in var_1:
        if word.count(app) % 2 != 0:
            nopair += app
            count += 1
    if count == 0:
        print("fully paired")
    else:
        print(nopair)
main()
