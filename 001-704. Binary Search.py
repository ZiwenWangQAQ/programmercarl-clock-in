class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left != right:
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right

            middle = (left + right) // 2
            if middle == left:
                if target == nums[left]:
                    return left
                if target == nums[right]:
                    return right
                return -1
            else:
                if target > nums[middle]:
                    left = middle
                else:
                    right = middle

        if nums[left] == target:
            return left
        else:
            return -1


