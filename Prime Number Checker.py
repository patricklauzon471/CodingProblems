def prime_checker(number):
    for i in range(2, number-1):
        if number % i == 0:
            print("It's not a prime number")
            exit()
        else:
            continue
    print("It's a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
