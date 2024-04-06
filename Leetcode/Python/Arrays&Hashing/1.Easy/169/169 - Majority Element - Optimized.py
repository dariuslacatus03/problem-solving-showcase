class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Second approach is to iterate through the list. Starting from the first
        # element, we save it and its count. If the next element is equal to the
        # saved element, increase count, if not, decrease count. If the count
        # becomes less than 0, change the current number.

        # Time complexity: O(n)
        # Extra space: O(1)

        count = 0
        res = None
        for el in nums:
            if el != res:
                if count == 0:
                    res = el
                    count = 1
                else:
                    count -= 1
            else:
                count += 1
        return res
