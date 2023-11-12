"""sequenceIII"""
def main():
    """printlinesasinput"""
    num = int(input())
    num_row = num
    num_column = num
    for row in range(num_row):
        for column in range(num_column):
            print(row + column + 2, end=" ")
        print()
main()
