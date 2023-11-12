"""triangle"""
def main(a_val, b_val, c_val):
    """decide if three lengths can build a Triangle or not"""
    if c_val == (a_val**2 + b_val**2)**0.5 or b_val == (a_val**2 + c_val**2)**0.5 \
        or a_val == (c_val**2 + b_val**2)**0.5:
        print("Yes")
    else:
        print("No")
main(float(input()), float(input()), float(input()))
