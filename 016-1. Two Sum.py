class Solution:
    def twoSum(self, num, target):
        hashtable = {}

        for i in range(len(num)):
            x = num[i]
            if target - x in hashtable:
                return (hashtable[target - x], i)
            hashtable[x] = i
