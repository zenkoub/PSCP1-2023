'''btsmrt'''
def main():
    """decideifPAYorFREE"""
    day = str(input())
    age = float(input())
    height = float(input())
    if day == "Children Day" and age < 14 and height <= 140:
        print("FREE")
    elif age < 14 and height < 90:
        print("FREE")
    elif day == "Senior Day" and age >= 60:
        print("FREE")
    else:
        print("PAY")
main()
