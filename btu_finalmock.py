'''finalmock'''
def main():
    '''btu'''
    area = int(input())
    height = int(input())
    person = int(input())
    room = input()
    sun = input()
    btu = 5000
    for i in range(height):
        if i > 8:
            btu += 1000
    for j in range(person):
        if j > 2:
            btu += 600
    if room == "kitchen":
        btu += 4000
    if room == "Normal":
        btu += 0
    if sun == "facing the sun":
        btu += (10/100)*btu
    if sun == "shaded":
        btu -= (10/100)*btu
    if sun == "Normal":
        btu += 0
    print(btu)

def areafirst(area):
    if area >= 100 and area <= 150:
        return 5000
    elif area >= 151 and area <= 250:
        return 6000
    elif area >= 251 and area <= 300:
        return 7000
    elif area >= 301 and area <= 350:
        return 8000
    elif area >= 351 and area <= 400:
        return 9000
    elif area >= 401 and area <= 450:
        return 10000
    elif area >= 451 and area <= 550:
        return 12000

def areasecond(area):
    if area >= 551 and area <= 700:
        return 14000
    elif area >= 701 and area <= 1000:
        return 18000
    elif area >= 1001 and area <= 1200:
        return 21000
    elif area >= 1201 and area <= 1400:
        return 23000
    elif area >= 1401 and area <= 1500:
        return 24000
    elif area >= 1501 and area <= 2000:
        return 30000
    elif area >= 2001 and area <= 2500:
        return 34000

main()