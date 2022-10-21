# Given two non-empty linked lists
# The digits are stored in reverse order
# Each node contains a single digit
# Add the two numbers and return the sum as a linked list

# Example1 l1 = [2,4,3] l2 = [5,6,4]
# output = [7,0,8] since 342 + 465 = 807

# process involves reversing each linked list, adding them, then reversing again
class Solution():
    def addTwoNumbers(self, l1, l2):

        # Each list is first reversed
        Newl1 = []
        for i in reversed(l1):
            Newl1.append(i)

        Newl2 = []
        for i in reversed(l2):
            Newl2.append(i)

        Output = []
        sum = 0

        # Need to add the two lists together digit by digit
        for i in range(len(l1)):
            sum = Newl1[i] + Newl2[i]
            Output.append(sum)
            sum = 0

        NewOutput = []
        for i in reversed(Output):
            NewOutput.append(i)
        return NewOutput


print(Solution().addTwoNumbers([2, 4, 3], [5, 5, 4]))
