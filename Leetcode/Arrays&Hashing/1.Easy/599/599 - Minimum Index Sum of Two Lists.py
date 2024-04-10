class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # Time complexity: O(n + m)
        # n - length of list1, m - length of list2

        wordsIndices = {}

        for i in range(len(list1)):
            wordsIndices[list1[i]] = i
        
        commons = {}
        
        minSum = 2003
        for i in range(len(list2)):
            if list2[i] in wordsIndices:
                commons[list2[i]] = i + wordsIndices[list2[i]]
                minSum = min(minSum, i + wordsIndices[list2[i]])
        res = []
        for key in commons:
            if commons[key] == minSum:
                res.append(key)
        
        return res