class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        dict1 = dict()
        dict2 = dict()

        for i in nums1:
            for j in nums2:
                k = i + j
                dict1[k] = dict1.setdefault(k, 0) + 1

        for i in nums3:
            for j in nums4:
                k = i + j
                dict2[k] = dict2.setdefault(k, 0) + 1

        res = 0

        for i, times in dict1.items():
            if 0 - i in dict2:
                res += times * dict2[0 - i]

        return res
