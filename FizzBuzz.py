# Takes number as an argument and returns "fizz" or "buzz"
# If the number is a multiple of 3 should return Fizz
# If the number is a multiple of 5 should return Buzz
# If the number is both should output FizzBuzz
# If neither the output should be the number inputted

def fizz_buzz(n):
    word = []
    for i in range(0, n):
        word.append(i)
        i += 1

    if len(word) % 3 == 0 and len(word) % 5 != 0:
        word = "fizz"
    elif len(word) % 5 == 0 and len(word) % 3 != 0:
        word = "buzz"
    elif len(word) % 3 == 0 and len(word) % 5 == 0:
        word = "fizzbuzz"
    else:
        word = n
    return word


print(fizz_buzz(15))
