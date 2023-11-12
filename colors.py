# '''colors'''
# def main(first, sec):
#     '''printthemixedcolor'''
#     if first == "Red":
#         print(red(first, sec))
#     elif first == "Yellow":
#         print(yellow(first, sec))
#     elif first == "Blue":
#         print(blue(first, sec))
#     else:
#         print(error(first, sec))

# def red(first, sec):
#     '''red'''
#     if first == "Red" and sec == "Yellow":
#         return "Orange"
#     elif first == "Red" and sec == "Blue":
#         return "Violet"
#     elif first == "Yellow" and sec == "Red":
#         return "Orange"
#     elif first == "Blue" and sec == "Red":
#         return "Violet"
#     elif first == "Red" and sec == "Red":
#         return "Red"

# def yellow(first, sec):
#     '''yellow'''
#     if first == "Yellow" and sec == "Blue":
#         return "Green"
#     elif first == "Yellow" and sec == "Red":
#         return "Orange"
#     elif first == "Blue" and sec == "Yellow":
#         return "Green"
#     elif first == "Red" and sec == "Yellow":
#         return "Orange"
#     elif first == "Yellow" and sec == "Yellow":
#         return "Yellow"

# def blue(first, sec):
#     '''blue'''
#     if first == "Blue" and sec == "Red":
#         return "Violet"
#     elif first == "Blue" and sec == "Yellow":
#         return "Green"
#     elif first == "Red" and sec == "Blue":
#         return "Violet"
#     elif first == "Yellow" and sec == "Blue":
#         return "Green"
#     elif first == "Blue" and sec == "Blue":
#         return "Blue"

# def error(first, sec):
#     '''error'''
#     if first != "Red" and sec == "Red":
#         return "Error"
#     elif first != "Yellow" and sec == "Yellow":
#         return "Error"
#     elif first != "Blue" and sec == "Blue":
#         return "Error"
#     elif first == "Red" and sec != "Red":
#         return "Error"
#     elif first == "Yellow" and sec != "Yellow":
#         return "Error"
#     elif first == "Blue" and sec != "Blue":
#         return "Error"

# main(input(), input())

'''colors'''
def color(first, sec):
    """ Drawing color function """
    list_color = ['Red', 'Yellow', 'Blue']
    if first not in list_color or sec not in list_color:
        print('Error')
    elif first == sec:
        print(first)
    elif (first == 'Red' and sec == 'Yellow') or (sec == 'Red' and first == 'Yellow'):
        print('Orange')
    elif (first == 'Red' and sec == 'Blue') or (sec == 'Red' and first == 'Blue'):
        print('Violet')
    elif (first == 'Blue' and sec == 'Yellow') or (sec == 'Blue' and first == 'Yellow'):
        print('Green')

def main():
    """ Main function """
    primary = input()
    secondary = input()
    color(primary, secondary)
main()
