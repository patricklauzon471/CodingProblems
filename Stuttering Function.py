def stutter(word):
    while True:
        if len(word) >= 3:
            break
        else:
            print('Word must be greater than 2 characters')
    letter = word[:2]
    phrase = '{} ... {} ... {}'.format(letter, letter, word)
    return phrase


print(stutter('apple'))
