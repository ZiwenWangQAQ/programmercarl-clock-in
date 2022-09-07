class Solution:
    def fourSum(self, nums, target):

        record_dict = dict()
        num_dict = dict()
        dupliacted_dict = dict()
        res = list()

        def if_existed(num1, num2, num3):
            if num1 in dupliacted_dict:
                if num2 in dupliacted_dict[num1]:
                    if num3 in dupliacted_dict[num1][num2]:
                        return False
                    else:
                        dupliacted_dict[num1][num2].add(num3)
                        return True
                else:
                    dupliacted_dict[num1][num2] = set()
                    dupliacted_dict[num1][num2].add(num3)
                    return True
            else:
                dupliacted_dict[num1] = dict()
                dupliacted_dict[num1][num2] = set()
                dupliacted_dict[num1][num2].add(num3)
                return True

        for num in nums:
            if num not in record_dict or record_dict[num] < 4:
                record_dict[num] = record_dict.setdefault(num, 0) + 1
        nums = []
        for num in record_dict:
            for k in range(record_dict[num]):
                nums.append(num)

        for i in range(len(nums)):
            num = nums[i]
            if num in num_dict:
                num_dict[num].append(i)
            else:
                num_dict[num] = [i]

        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                for k in range(j + 1, len(nums)):
                    num3 = nums[k]
                    num4 = target - num1 - num2 - num3

                    if num4 in num_dict:
                        for l in num_dict[num4]:
                            if l > k:
                                new_ans = [num1, num2, num3, num4]
                                new_ans.sort()
                                if if_existed(new_ans[0], new_ans[1], new_ans[2]):
                                    res.append(new_ans)
        return res