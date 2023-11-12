"""One-Sided Pyramid"""
def main():
    """One-Sided Pyramid"""
    size = int(input())
    for i in range(size):
        for j in range(size):
            if j >= size-i-1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()
main()
