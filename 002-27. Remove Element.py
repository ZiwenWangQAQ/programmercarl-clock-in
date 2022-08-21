class Solution:
    def removeElement(self, nums, val):
        flag = False
        length = len(nums)
        while not flag:
            flag = True
            for i in range(length):
                if nums[i] == val:
                    nums[i], nums[length - 1] = nums[length - 1], nums[i]
                    length = length - 1
                    flag = False
                    break

        return length
