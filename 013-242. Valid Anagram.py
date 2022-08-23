class Solution:
    def isAnagram(self, s, t):
        record = dict()
        for i in s:
            record[i] = record.setdefault(i, 0) + 1
        for i in t:
            if i not in record:
                return False
            else:
                record[i] -= 1
                if record[i] == 0:
                    del record[i]
        if record:
            return False

        return True
