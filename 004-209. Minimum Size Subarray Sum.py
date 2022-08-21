class Solution:
    def minSubArrayLen(self, target, nums):
        head = 0
        tail = 0
        total = 0
        ans = -1
        length = len(nums)
        while head <= tail < length:
            total = total + nums[tail]
            if total >= target:
                if ans == -1:
                    ans = tail - head + 1
                else:
                    ans = min(ans, tail - head + 1)
                total = total - nums[head]
                total = total - nums[tail]
                head += 1
            else:
                tail = tail + 1

        if ans == -1:
            return 0
        else:
            return ans
