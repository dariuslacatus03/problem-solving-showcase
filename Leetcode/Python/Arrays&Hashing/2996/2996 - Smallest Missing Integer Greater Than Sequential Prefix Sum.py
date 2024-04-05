class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort the list, and while you iterate through it, save the appearances and
        # look for the longest sequential prefix and calculate its sum, then look
        # in the constructed map to find the smallest number larger or equal to sum
        # Time complexity: O(n)

        appearances = {}
        appearances[nums[0]] = 1
        seqSum = nums[0]
        inSeq = 1
        i = 1
        while i < len(nums):
            if nums[i] in appearances:
                appearances[nums[i]] += 1
            else:
                appearances[nums[i]] = 1

            if inSeq == 1 and nums[i - 1] == nums[i] - 1:
                seqSum += nums[i]
            else:
                inSeq = 0
            i += 1

        while seqSum in appearances:
            seqSum += 1

        return seqSum



