class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Time complexity: O(n)
        
        freq = set()
        for num in nums:
            if num not in freq:
                freq.add(num)
            else:
                return num

