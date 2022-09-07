class Solution:
    def reverseStr(self, s, k):
        if k == 1:
            return s

        ans = ''
        for i in range(0, len(s) + 2 * k, 2 * k):
            str_part = s[i:i + k]

            # ans+=str_part[::-1] this is a easy way to get the reversed string
            for j in range(len(str_part) - 1, -1, -1):
                ans += str_part[j]

            ans += s[i + k:i + 2 * k]

        return ans
