class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Iterate and save the values in a hashset, if a value already exists
        # in our hashset, return True. If we don't find any repeated value => False

        hashset = set()

        for el in nums:
            if el in hashset:
                return True
            hashset.add(el)

        return False