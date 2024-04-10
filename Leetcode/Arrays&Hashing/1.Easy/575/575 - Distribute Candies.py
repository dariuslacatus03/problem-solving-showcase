class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        #Time complexity O(n)
        # n - length of candyType
        
        candyTypes = set(candyType)
        
        canEat = len(candyType)//2

        return min(canEat, len(candyTypes))
        