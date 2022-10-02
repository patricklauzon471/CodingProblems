# Given an integer n return true if its a power of two
# Otherwise return false
# Example1 n = 1, output = True, 2^0 = 1

# If a number is odd besides 1 it is not a power of two
# numbers that are even are not neccessarily powers of 2

class Solution():
    def isPowerOfTwo(self, n):

        # Check if the number is even
        # If it's not then the condition is automatically false
        if n % 2 != 0:
            return False

        # Need to create a loop to divide numbers by 2
        # Every number that's a power of two and is divided by 2 will evenbtually simplify to 1
        # If the number is one return True, else return false

        while n % 2 == 0:
            n = n / 2

        if n == 1:
            return True
        else:
            return False


print(Solution().isPowerOfTwo(4))
