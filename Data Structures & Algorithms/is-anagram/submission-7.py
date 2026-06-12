class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_s, dic_t = {}, {}
        for letter in s:
            dic_s[letter] = dic_s.get(letter, 0) + 1
        for letter in t:
            dic_t[letter] = dic_t.get(letter, 0) + 1
        
        return dic_s == dic_t
        for key in dic_s:
            if dic_t.get(key,0) != dic_s[key]:
                return False
        return len(dic_s) == len(dic_t)