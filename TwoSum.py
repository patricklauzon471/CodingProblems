# Given integer of nums and an integer target
# Return indices such that they add up to the target

#nums = [2, 7, 11, 15]
#target = 9

class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return ([nums[i], nums[j]])

        return []


print(Solution().twoSum([2, 11, 7, 15], 9))
