class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = set()
        f = 0
        res = 0
        for l in range(len(s)):
            while s[l] in dic:
                    dic.remove(s[f])
                    f += 1
            dic.add(s[l])        
            res = max(res, l - f + 1)    
        return res