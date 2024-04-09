class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Construct a set with values from 1 to n, then iterate through nums and
        # eliminate every element that is contained in the set
        # Time complexity: O(n)
        # Extra space: O(n)


        res = set()

        for el in range(1, len(nums) + 1):
            res.add(el)
        for el in nums:
            if el in res:
                res.discard(el)

        return res
        