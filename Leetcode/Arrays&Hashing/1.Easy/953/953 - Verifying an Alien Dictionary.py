class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Time complexity: O(n)
        # n - length of characters in list
        i = 0
        newOrder = {}
        for char in order:
            newOrder[char] = i
            i += 1
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if newOrder[word2[j]] < newOrder[word1[j]]:
                        return False
                    break
        return True
