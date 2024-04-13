class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        #Time complexity: O(n)

        freq = {}
        maxFreq = 0
        res = ""
        for word in paragraph.lower().replace(",", " ").split():
            word = word.strip("!?',;.")
            if word not in banned:
                if word not in freq:
                    freq[word] = 1
                    if maxFreq < freq[word]:
                        maxFreq = freq[word]
                        res = word
                else:
                    freq[word] += 1
                    if maxFreq < freq[word]:
                        maxFreq = freq[word]
                        res = word
        
        return res

            