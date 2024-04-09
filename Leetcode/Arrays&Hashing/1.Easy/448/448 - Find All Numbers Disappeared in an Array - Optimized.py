class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Optimized: Our list contains values from 1 to n. The indices are from
        # 0 to n-1. Map every number n found to abs(n-1) and change the value from 
        # that position to the negative of its absolute. Then iterate through the list
        # and for every positive number found, add to the result list the index+1
        # (If we have a positive number on a position it means that we didn't find
        # the number index+1 in our list)
        
        # Time complexity: O(n)
        # Extra space: O(1) if we don't take into account the res list

        for el in nums:
            i = abs(el) - 1
            nums[i] = -1 * abs(nums[i])
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        
        return res
        
