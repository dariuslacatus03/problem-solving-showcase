class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sum of terms from 1 to n = (n*(n+1))/2. Since nums will contain distinct
        # numbers in [0, n], we just have to return sum of terms from 1 to n - sum
        # of all elements from nums

        sumFirstN = (len(nums) * (len(nums) + 1))//2
        numsSum = 0
        for el in nums:
            numsSum += el

        return sumFirstN - numsSum