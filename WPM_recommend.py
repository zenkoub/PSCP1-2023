'''WPM'''
def main(gen, wpm):
    '''recommend'''
    if gen == "Kids":
        print(kid(gen, wpm))
    elif gen == "Adults":
        print(adult(gen, wpm))

def kid(gen, wpm):
    '''kids'''
    if gen == "Kids":
        if wpm < 11:
            return "Very Slow"
        elif wpm >= 11 and wpm <= 20:
            return "Slow"
        elif wpm >= 21 and wpm <= 30:
            return "Average"
        elif wpm >= 31 and wpm <= 40:
            return "Fast"
        elif wpm > 40:
            return "Very Fast"

def adult(gen, wpm):
    '''adults'''
    if gen == "Adults":
        if wpm < 26:
            return "Very Slow"
        elif wpm >= 26 and wpm <= 35:
            return "Slow/Beginner"
        elif wpm >= 36 and wpm <= 45:
            return "Intermediate/Average"
        elif wpm >= 46 and wpm <= 65:
            return "Fast/Advanced"
        elif wpm >= 66 and wpm <= 80:
            return "Very Fast"
        elif wpm > 80:
            return "Insane"

main(input(), int(input()))
