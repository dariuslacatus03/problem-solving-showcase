class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # First approach is to iterate through the list and save the appearances
        # Time complexity: O(n)
        # Extra space: O(n)

        appearances = {}
        for el in nums:
            if el in appearances:
                appearances[el] += 1
            else:
                appearances[el] = 1

        for key in appearances:
            if appearances[key] > len(nums) / 2:
                return key