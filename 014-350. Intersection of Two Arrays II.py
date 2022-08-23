class Solution:
    def intersect(self, nums1, nums2):
        record1 = [0] * 1001
        record2 = [0] * 1001
        for num in nums1:
            record1[num] += 1
        for num in nums2:
            record2[num] += 1

        ans = list()
        for i in range(len(record1)):
            if record1[i] and record2[i]:
                num = min(record1[i], record2[i])
                for j in range(num):
                    ans.append(i)

        return ans
