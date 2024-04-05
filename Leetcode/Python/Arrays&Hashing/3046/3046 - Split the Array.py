class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # First approach is to sort the list then iterate through it and
        # check for triplets
        # Time complexity: O(n*logn + n)

        # Sort time complexity: O(n logn)
        nums.sort()

        lastPopped = 0
        count = 0
        # Search for triplets time comlexity: O(n)
        while nums:
            last = nums.pop()
            if last == lastPopped:
                count = count + 1
                if count == 3:
                    return False
            else:
                count = 1
                lastPopped = last

        return True