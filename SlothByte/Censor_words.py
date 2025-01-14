def censor(s):
    words = s.split(' ')
    
    for i, word in enumerate(words):
        if len(word) > 4:
            censored = ['*' for j in range(0,len(word))]
            words[i] = ''.join(str(x) for x in censored)
    
    censored_s = ' '.join(str(i) for i in words)
    return censored_s

if __name__ == "__main__":
    print(censor("The code is fourty"))
    print(censor("Two plus three is five"))
    print(censor("aaaa aaaaa 1234 12345"))