class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # First approach is to iterate through the list and for each element, we
        # iterate through the remaining elements of the list, searching for a pair
        # to be added so that the sum is equal to target

        # Time complexity: O(n^2)

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



