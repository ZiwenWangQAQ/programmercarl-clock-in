class Solution:
    def isHappy(self, n):
        record = set()
        while n != 1:
            num_list = list()
            while n:
                num_list.append(n % 10)
                n = n // 10
            sum_of_squre = 0
            for num in num_list:
                sum_of_squre += num * num

            if sum_of_squre in record:
                return False

            record.add(sum_of_squre)
            n = sum_of_squre

        return True
