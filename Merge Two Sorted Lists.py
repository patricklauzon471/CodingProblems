# Given two linked lists, list1 and list2
# merge the two lists into one sorted list made by splicing together nodes

# Example list1 = [1,2,4] list2 = [1,3,4]
#Output = [1,1,2,3,4,4]

class Solution():
    def mergeTwoLists(self, list1, list2):
        # output ius initialized as an empty list
        output = []
        # While neither list 1 or list 2 are empty
        while list1 and list2:
            # If the first number in list1 is less than list2 append the first number from list1
            # This number is also removed from list1 which will eventually reduce to 0
            if list1[0] < list2[0]:
                output.append(list1.pop(0))
            else:
                output.append(list2.pop(0))
        output += list1
        output += list2
        return output


print(Solution().mergeTwoLists([1, 2, 4], [1, 3, 4]))
