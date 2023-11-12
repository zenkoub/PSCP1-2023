"""jp"""
def main():
    """jp"""
    bun1 = "|"
    bun2 = "|"
    meatt = "*"
    leftbun = int(input())
    rightbun = int(input())
    meat = (leftbun + rightbun) * 2
    print(bun1 * leftbun + meatt * meat + bun2 * rightbun)
main()
