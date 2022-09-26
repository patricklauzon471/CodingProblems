# Given an integer array nums
# Return true if any value appears at least twice
# Return false if every element is distinct

class Solution():
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


print(Solution().containsDuplicate([1, 2, 1, 4]))
