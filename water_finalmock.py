'''water_finalmock'''
def main():
    '''printoutthetotal'''
    month = int(input())
    cost = float(input())
    volume = float(input())
    upcost = float(input())
    limit = float(input())
    total = 0
    for _ in range(month):
        used = float(input())
    if used < volume:
        total += used*cost
    if used > volume:
        total += (used - volume)*upcost
    if (cost*used) < limit:
        total += 0
    print(total)

main()
