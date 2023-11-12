'''removetag'''
def main():
    '''removehtmltagandformatinto'''
    message = str(input())
    list_n = []
    list_n.append(message)
    
    list_n.remove("<")
    print(list_n)
main()