# Need to break a nested loop using a condition
for i in range(6):
    for j in range(6):
        if j == i:
            break
        print(i, j)
# Prints a matrix that stops when j = 5
