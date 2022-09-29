# Given a string s containing the characters () {} []
# Determine if the input string is valid

class Solution():
    def isValid(self, s):
        # The input s has to follow this pattern
        # can correspond the order of the s input to this created list order
        order = ["(", ")", "{", "}", "[", "]"]
        # Check immediately if the first inputs match, if not return False
        if s[0] != order[0]:
            return False
        # Cycle through the inputs in the list
        for i in range(len(s)):
            # if the inputs match continue to cycle through until every input
            # has been checked if all inputs are valid break the for loop
            # and return true
            if s[i] == order[i]:
                continue
            else:
                return False

        return True


print(Solution().isValid(["(", ")", "{", "}"]))
