'''lift'''
def main():
    '''printoutifsafeofnot'''
    person = int(input())
    leverage = float(input())
    for i in range(person):
        is_age = int(input())
        is_weight = float(input())
    if is_age < 12:
        print("Not Safe")
    elif is_weight > leverage:
        print("Not Safe")
    else:
        print("Safe")
main()

# # must indicate sum of weight
# if sum_weight > leverage:
#     return "Not Safe"

# # anyone under 12 must have 1 standby grownup
# if all_age < 12:
#     return "Not Safe"