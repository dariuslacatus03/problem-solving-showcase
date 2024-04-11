class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        #Time complexity: O(n + n*m)
        # n - len(licensePlate)
        # m - length of words
        letters = {}
        for char in licensePlate:
            if char.isalpha():
                char = char.lower()
                if char not in letters:
                    letters[char] = 1
                else:
                    letters[char] += 1
        minLength = 16
        verifier = {}
        for word in words:
            verifier.clear()
            completing = 1
            for letter in word:
                if letter in letters:
                    if letter not in verifier:
                        verifier[letter] = 1
                    else:
                        verifier[letter] += 1
            if len(letters) == len(verifier):
                for letter in letters:
                    if letters[letter] > verifier[letter]:
                        completing = 0
            else:
                completing = 0
            if completing == 1:
                if len(word) < minLength:
                    minLength = len(word)
                    minWord = word
        return minWord