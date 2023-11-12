'''bogframe'''
def main():
    '''printoutasequenceofasterisksandinputtext'''
    word1 = input().rstrip()
    word2 = input().rstrip()
    word3 = input().rstrip()
    word4 = input().rstrip()
    word5 = input().rstrip()
    long = max(len(word1), len(word2), \
len(word3), len(word4), len(word5))
    print("**"+"*"*long+"**")
    print("* "+word1+" "*(long-len(word1))+" *")
    print("* "+word2+" "*(long-len(word2))+" *")
    print("* "+word3+" "*(long-len(word3))+" *")
    print("* "+word4+" "*(long-len(word4))+" *")
    print("* "+word5+" "*(long-len(word5))+" *")
    print("**"+"*"*long+"**")
main()
