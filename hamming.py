'''hamming'''
def main():
    '''countthetimesofconvertings'''
    word_1 = input()
    word_2 = input()
    answer = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            answer += 1
    print(answer)
main()
