class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Iterate through all the numbers and save the number of appearances
        # and the max frequency, then iterate through the map and find the sum
        # of all items with the frequency equal to the max frequency
        # Time complexity: O(n)

        appearances = {}
        maxFreq = 1
        for el in nums:
            if el in appearances:
                appearances[el] += 1
                if appearances[el] > maxFreq:
                    maxFreq = appearances[el]
            else:
                appearances[el] = 1

        totalFreq = 0
        for key in appearances:
            if appearances[key] == maxFreq:
                totalFreq += maxFreq

        return totalFreq