class Solution:
    def canConstruct(self, ransomNote, magazine):
        dict_ransom = dict()
        for letter in ransomNote:
            dict_ransom[letter] = dict_ransom.setdefault(letter, 0) + 1

        for letter in magazine:
            if letter in dict_ransom:
                dict_ransom[letter] -= 1
                if dict_ransom[letter] == 0:
                    del dict_ransom[letter]

        if not dict_ransom:
            return True
        else:
            return False
