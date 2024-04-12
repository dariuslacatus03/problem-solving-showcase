class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #Time complexity: O(n)
        # n - total number of letters in the list words

        morseLetters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        freq = {}
        for word in words:
            asciiWord = ""
            for letter in word:
                asciiWord += morseLetters[ord(letter) - ord("a")]
            if asciiWord not in freq:
                freq[asciiWord] = 1
            else:
                freq[asciiWord] += 1
        
        return len(freq)