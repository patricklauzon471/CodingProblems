def find_sum(n):
    # Set a base condition
    if n == 1:
        return 1
    # Have the function return the input plus a number less than the input
    # This will continue looping until the number hits the base condition
    # If the base condition is not set this would loop forever
    # loops because the function is used inside the function decremented by 1
    return n + find_sum(n-1)


print(find_sum(10))
