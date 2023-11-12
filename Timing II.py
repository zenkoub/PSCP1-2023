"""Timing II"""
def main():
    """timing"""
    seconds = int(input())
    minutes = seconds//60
    seconds = seconds%60
    hours = minutes//60
    minutes = minutes%60
    days = hours//24
    hours = hours%24
    if days > 9999:
        print("ERR_:__:__:__")
    else:
        print("{:04d}:{:02d}:{:02d}:{:02d}".format(days, hours, minutes, seconds))
main()
