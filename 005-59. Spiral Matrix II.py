class Solution:
    def generateMatrix(self, n):
        if n == 1:
            return [[1]]

        ans = list()
        for i in range(n):
            ans.append([0] * n)

        num = 0
        x_place = 0
        y_place = 0
        final_num = n * n
        while num < final_num:
            for i in range(n - 1):
                num += 1
                ans[x_place][y_place] = num
                y_place += 1

            for i in range(n - 1):
                num += 1
                ans[x_place][y_place] = num
                x_place += 1
            for i in range(n - 1):
                num += 1
                ans[x_place][y_place] = num
                y_place -= 1
            for i in range(n - 1):
                num += 1
                ans[x_place][y_place] = num
                x_place -= 1

            x_place += 1
            y_place += 1
            n = n - 2

            if n == 1:
                num = num + 1
                ans[x_place][y_place] = num

        return ans
