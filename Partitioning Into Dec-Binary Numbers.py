# Decimal number is called deci-binary either 0 or 1
# For example 101 and 1100 while 112 and 3001 are not

# Given a string n that represents a positive decimal integer

# Understand the math behind the question
# The output will always be equal to the largest digit in the number
# For 8514 the output will be 8 because 10,000 overshoots so can only increment by 1000s

class Solution():
    def minPartitions(self, n):
        # Convert the string to a list
        num = list(n)
        # Iterate through the list and return the largest digit
        for i in range(len(num)):
            numMax = max(num[i])
        return numMax


print(Solution().minPartitions('125'))
