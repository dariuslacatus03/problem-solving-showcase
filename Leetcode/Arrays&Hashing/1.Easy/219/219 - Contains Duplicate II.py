class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Iterate and save in map the position where each item appeared.
        # When a number appeared again, check the absolute difference
        # between its index and the index of the last appearance.

        #Time complexity: O(n)
        #Extra space: O(n)

        appeared = {}

        for i in range(len(nums)):
            if nums[i] in appeared:
                if abs(appeared[nums[i]] - i) <= k:
                    return True
            appeared[nums[i]] = i

        return False
