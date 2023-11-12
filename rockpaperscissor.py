'''rockpaperscissor'''
def main():
    '''countscore'''
    message = str(input())
    total = len(message)
    val_a = 0
    val_b = 0
    for i in range(2, total + 1, + 2):
        cut = message[i-2:i]
        if cut == "RP":
            val_a += 1
        elif cut == "PR":
            val_b += 1
        elif cut == "PS":
            val_a += 1
        elif cut == "SP":
            val_b += 1
        elif cut == "RP":
            val_a += 1
        elif cut == "PR":
            val_b += 1
        elif cut == "SR":
            val_a += 1
        elif cut == "RS":
            val_b += 1
        else:
            val_a += 0
            val_b += 0
    result(val_a, val_b)

def result(val_a, val_b):
    '''printoutscoreconclusion'''
    if val_a < val_b:
        print("A win", "%d-%d" % (val_b, val_a))
    elif val_a == val_b:
        print("DRAW", val_b)
    elif val_a > val_b:
        print("B win", "%d-%d" % (val_a, val_b))
main()
