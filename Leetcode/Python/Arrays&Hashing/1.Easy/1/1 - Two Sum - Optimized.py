class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Second approach is to iterate through the list and save the indices
        # in a hashmap. For each element we must check if we have the value
        # target - element in our hashmap

        # Time complexity: O(n)
        # Extra space: O(n)

        appearances = {}

        for i in range(len(nums)):
            if target - nums[i] in appearances:
                return [i, appearances[target - nums[i]]]
            appearances[nums[i]] = i









