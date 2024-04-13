class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        """
        :type deck: List[int]
        :rtype: bool
        """
        # Time complexity: O(n)
        freq = {}

        for card in deck:
            if card not in freq:
                freq[card] = 1
            else:
                freq[card] += 1
        checkWith = freq[deck[0]]
        for key in freq:
            checkWith = gcd(checkWith, freq[key])
        return checkWith > 1