"""compositefunc"""
def main():
    """eiei"""
    num = float(input())
    func = input()
    func = func.lower()
    if func == "fog":
        result_1 = num**3+4*num-1
        result_2 = (15+result_1-result_1**3)/(result_1**2/3+11)
        print("%.2f" %result_2)
    if func == "gof":
        result_3 = (15+num-num**3)/(num**2/3+11)
        result_4 = result_3**3+4*result_3-1
        print("%.2f" %result_4)
main()
