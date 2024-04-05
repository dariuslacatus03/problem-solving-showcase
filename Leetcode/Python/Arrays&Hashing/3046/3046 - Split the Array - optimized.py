class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Second approach is to iterate through the list and save the number of
        # appearances in a hashmap. Then iterate through hashmap and see if any
        # number appeared more than two times

        # Time complexity: O(n)
        # Extra space: O(n)

        appearances = {}
        # Dictionary lookups and inserts have O(1) time complexity
        # so this for loop has O(n) time complexity
        for el in nums:
            if el in appearances:
                appearances[el] += 1
                if appearances[el] > 2:
                    return False
            else:
                appearances[el] = 1

        return True