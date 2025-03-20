def turnCalc(number):
    number = str(number)
    letters = ['O', 'I', 'Z', 'E', 'H', 'S', 'G', 'L', 'B']
    word = []

    for i in number:
        word.append(letters[int(i)])
    
    word.reverse()
    res = ''.join(word)
    return res

if __name__ == "__main__":
    print(turnCalc(707))
    print(turnCalc(5508))
    print(turnCalc(3045))
    print(turnCalc("07734"))