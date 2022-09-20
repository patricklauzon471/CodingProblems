# Given root of a binary tree
# Return its maximum depth
# Max depth is the number of nodes along the longest path from the root down to the farthest leaf

# Example1 root = [3, 9, 20, null, null, 15, 7] returns 3
# Example2 root = [1, null, 2] returns 2

# class TreeNode():
#     def __init__(self, val = 0, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution():
    def maxDepth(self, root):
        # Initialize count which will be the number that tracks output
        count = 1
        # will cycle for the length of root
        for i in range(len(root)):
            if root[i] < root[i+1]:
                count += 1
            elif root[i] > root[i+1]:
                # leave the loop if the number in the list is larger than the next
                # This will return the current count number
                break
            i += 1
        return count


print(Solution().maxDepth([1, 2, 5, 6, 0, 12]))
