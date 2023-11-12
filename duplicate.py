'''duplicateI'''
def main(quan_a, quan_b):
    '''printoutintersectmembersfrombothgroups'''
    set_a = set()
    set_b = set()
    for _ in range(quan_a):
        studentnum_a = input()
        set_a.add(studentnum_a)
    for _ in range(quan_b):
        studentnum_b = input()
        set_b.add(studentnum_b)
    duplicates = list(set_a.intersection(set_b))
    duplicates.sort(reverse=True)
    if duplicates == []:
        print("Nope")
    else:
        print(*duplicates, sep="\n")

main(int(input()), int(input()))
