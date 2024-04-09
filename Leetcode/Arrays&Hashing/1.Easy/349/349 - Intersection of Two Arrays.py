class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        res = set()

        for el in nums2:
            if el in nums1:
                res.add(el)

        return res

        # OR

        # res = {}

        # for el in nums2:
        #     if el in nums1:
        #         res[el] = 1

        # return res.keys()