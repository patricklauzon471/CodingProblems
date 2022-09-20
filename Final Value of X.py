# Programming language only four operations and one variable X
# ++X and X++ increments the value of X by 1
# --X and X-- decrements the value of X by one

# Given string of operators return the final value of X

class Solution():
    def finalValueAfterOperations(self, operations):
        x = 0
        for i in range(len(operations)):
            if operations[i] == 'X++' or operations[i] == '++X':
                x += 1
            elif operations[i] == 'X--' or operations[i] == '--X':
                x -= 1
        return x


print(Solution().finalValueAfterOperations(['X++', 'X--', 'X++']))
