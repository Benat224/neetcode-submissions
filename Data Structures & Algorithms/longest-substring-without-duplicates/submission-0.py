class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = set()
        f = 0
        l = 0
        res = 0
        while l < len(s):
            if s[l] in dic:
                while s[f] != s[l]:
                    dic.remove(s[f])
                    f += 1
                f += 1
            else:
                dic.add(s[l])        
            l += 1
            res = max(res, l - f)    
        return res