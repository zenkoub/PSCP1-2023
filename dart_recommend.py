'''recommmend'''
def main(num):
    '''dart'''
    score = 0
    for _ in range(num):
        point = input().split()
        pointx = int(point[0])
        pointy = int(point[1])
        shoot = (pointx**2 + pointy**2)**0.5
        if shoot <= 2:
            score += 5
        elif shoot <= 4:
            score += 4
        elif shoot <= 6:
            score += 3
        elif shoot <= 8:
            score += 2
        elif shoot <= 10:
            score += 1
    print(score)
main(int(input()))
