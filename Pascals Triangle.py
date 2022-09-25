# Given an integer number of rows
# In Pascals traingle each number is the sum of the two numbers above it

# Example1 umrows = 5
#Output = [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]

class Solution():
    def generate(self, numrows):
        row1 = [[1]]
        if numrows == 1:
            return 1
        else:
            for i in range(numrows-1):
                row2 = [0] + row1[-1] + [0]
                row = []
                for j in range(len(row1[-1])+1):
                    row.append(row2[j] + row2[j + 1])
                row1.append(row)
            return row1


print(Solution().generate(3))
