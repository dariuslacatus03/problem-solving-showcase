class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Time complexity: O(n)

        freq = {}
        res = []
        sumAll = 0
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
                sumAll += nums[i]
            else:
                freq[nums[i]] += 1
                res.append(nums[i])

        res.append(len(nums)*(len(nums)+1)/2 - sumAll)

        return res