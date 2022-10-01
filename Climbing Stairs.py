# You are climbing stairs, it takes n steps to reach the top
# Each time you can either climb 1 or 2 steps, how many distinct ways can you climb to the top

# Example1 n=2, output = 2
# Example2 n = 3, output = 3

# Solve using dynamic programming
# Start at the last number and count backwards
# Base case starts at the number 1
# At the previous number there can only be 1 possible move to get to the final
# every other value in the range has 2 possible moves
# Start the count at 1, the number closest to the final will add 1 to the count
# Every other nunber will add 2


class Solution():
    def climbStairs(self, n):
        count = 2

        if n == 2:
            return count

        elif n == 1:
            count = 1
            return count

        else:
            for i in range(n-2):
                count += 2
                i += 1
            return count


print(Solution().climbStairs(1))
