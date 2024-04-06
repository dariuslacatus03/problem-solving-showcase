class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Save appearances of elements from nums1, then iterate through elements of
        # nums2 and everytime you find an element from nums1, decrease its value from
        # appearances


        nums1Apps = {}

        for el in nums1:
            if el in nums1Apps:
                nums1Apps[el] += 1
            else:
                nums1Apps[el] = 1
        
        res = []

        for el in nums2:
            if el in nums1Apps and nums1Apps[el] > 0:
                res.append(el)
                nums1Apps[el] -= 1

        return res