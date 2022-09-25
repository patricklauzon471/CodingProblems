# Given the head of a singly linked list reverse the list and return the reversed value
# example1 head = [1,2,3,4,5]
#output = [5,4,3,2,1]

class Solution():
    def reverseList(self, head):
        i = len(head)
        output = []
        while i > 0:
            output.append(head[i-1])
            i -= 1
        return output


print(Solution().reverseList([1, 2, 3, 4, 5]))
