class Solution:
    def threeSum(self, nums):
        record_dict = dict()
        for i in nums:
            if i in record_dict:
                if record_dict[i] < 3:
                    record_dict[i] += 1
            else:
                record_dict[i] = 1
        nums = []
        for i in record_dict:
            for j in range(record_dict[i]):
                nums.append(i)

        res = list()
        res_set = set()
        dic_nums = dict()
        duplicated_dict = dict()
        for i in range(len(nums)):
            num = nums[i]
            dic_nums.setdefault(num, list()).append(i)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num1 = nums[i]
                num2 = nums[j]
                target = 0 - num1 - num2
                if target in dic_nums:
                    for k in dic_nums[target]:
                        if k > i and k > j:
                            new_ans = [num1, num2, target]
                            new_ans.sort()
                            s1, s2 = new_ans[0], new_ans[1]
                            if s1 in duplicated_dict:
                                if s2 in duplicated_dict[s1]:
                                    continue
                                else:
                                    duplicated_dict[s1].add(s2)
                                    res.append(new_ans)
                            else:
                                duplicated_dict[s1] = set()
                                duplicated_dict[s1].add(s2)
                                res.append(new_ans)

        return res