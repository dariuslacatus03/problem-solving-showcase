class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        #Time complexity: O(n*m)
        # n - length of nums2, m - length of words

        res = []

        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')

        for word in words:
            wordLower = set(word.lower())
            if wordLower.issubset(row1):
                res.append(word)
                continue
            if wordLower.issubset(row2):
                res.append(word)
                continue
            if wordLower.issubset(row3):
                res.append(word)
                continue
            
		
        return res