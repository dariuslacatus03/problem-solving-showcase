class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # For every item in nums1, iterate through all the items in nums2. Search
        # for the element in nums1, remember that you found it, then search for
        # an element greater than the one from nums1

        #Time complexity: O(n*m)
        
        res = []
        
        for i in range(len(nums1)):
            found = 0
            greater = 0
            j = 0
            while greater == 0 and j < len(nums2):
                if found == 1 and nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    greater = 1
                if nums1[i] == nums2[j]:
                    found = 1
                j += 1
            if greater == 0:
                res.append(-1)

        return res
