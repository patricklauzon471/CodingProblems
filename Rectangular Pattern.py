# Need to print a 5 row 3 column output of the stars

symbol = ['*', '*', '*', '*', '*']

for sym in symbol:
    count = 0
    while count < 3:
        print(sym, end=' ')
        count = count + 1
    print()
