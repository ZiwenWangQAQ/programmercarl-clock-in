class Solution:
    def sortedSquares(self, nums):
        length = len(nums)
        ans = [0] * length

        head = 0
        tail = length - 1
        while head <= tail:
            if abs(nums[head]) > abs(nums[tail]):
                ans[length - 1] = nums[head] * nums[head]
                head += 1
            else:
                ans[length - 1] = nums[tail] * nums[tail]
                tail -= 1
            length -= 1

        return ans
