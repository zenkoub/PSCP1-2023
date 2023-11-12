'''stair'''
def main():
    '''leaststeps'''
    step = int(input())
    stair = int(input())
    threesteps = 0
    var_1 = 0
    out = 0
    for _ in range(stair):
        heightstair = int(input())
        var_1 = heightstair + var_1
        if heightstair > step:
            out = 1
        elif var_1 == step:
            threesteps += 1
            var_1 = 0
        elif var_1 > step:
            threesteps += 1
            var_1 = heightstair
    if var_1 > 0:
        threesteps += 1
    if out == 1:
        print("NO")
    else:
        print(threesteps)
main()
