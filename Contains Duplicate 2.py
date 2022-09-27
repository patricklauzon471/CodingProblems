# Given an integer array nums and an integer k return true if there are two distinct indices
# i and j in the array such that nums[i] == nums[j] and abs(i-j) <= k


class Solution():
    def containsNearbyDuplicate(self, nums, k):
        # i loops through the list
        for i in range(len(nums)):
            # j loops through the list one index away from i, allowing it to check every number besides
            # i and return true if there's a match
            # Need to also go through array and check if any value is less than k
            for j in range(i+1, len(nums)):
                absolute = abs(i-j)
                if nums[i] == nums[j]:
                    if absolute > k:
                        return False
                    return True
        return False


print(Solution().containsNearbyDuplicate([1, 3, 1, 4], 2))
