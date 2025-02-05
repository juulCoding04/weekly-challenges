def doesRhyme(s1, s2):
    last1 = s1.lower().replace('!', '').replace('.', '').replace('?', '').split()[-1]
    last2 = s2.lower().replace('!', '').replace('.', '').replace('?', '').split()[-1]

    if last1 in last2:
        return True
    elif last2 in last1:
        return True
    else:
        return False


if __name__ == "__main__":
    print(doesRhyme("Sam I am!", "Green eggs and ham."))
    print(doesRhyme("Sam I am!", "Green eggs and HAM."))
    print(doesRhyme("You're built like a seat", "I bet you like to eat"))
    print(doesRhyme("You are off to the races", "a splendid day."))
    print(doesRhyme("and frequently do?", "you gotta move."))