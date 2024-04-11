class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Time complexity: O(n)
        #Extra space: O(n)
        freq = {}
        firstSeen = {}
        maxFreq = 0
        minLength = 0
        for i in range(len(nums)):
            if nums[i] not in firstSeen:
                firstSeen[nums[i]] = i

            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
            if freq[nums[i]] > maxFreq:
                maxFreq = freq[nums[i]]
                minLength = i - firstSeen[nums[i]] + 1
            elif freq[nums[i]] == maxFreq:
                minLength = min(minLength, i - firstSeen[nums[i]] + 1)
        
        return minLength
       
