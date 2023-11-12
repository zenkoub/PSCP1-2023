"""weightstation"""
def main():
    """weightstation"""
    average = float(input())
    second = float(input())
    third = float(input())
    fourth = float(input())
    first = 4*average - second - third - fourth
    result = first + second + third + fourth
    if result > 15000:
        print("Overweight")
    elif abs(first-average) > 0.5*average or abs(second-average) > 0.5*average or \
        abs(third-average) > 0.5*average or abs(fourth-average) > 0.5*average:
        print("Unbalance")
    else:
        print("Pass", "%.2f" % first)
main()

# first = 1000
# second = 2000
# third = 3000
# fourth = 4000
# sum = 10000, 10 tonnes
# average = (1000 + 2000 + 3000 + 4000)/4
    # average = 2500
