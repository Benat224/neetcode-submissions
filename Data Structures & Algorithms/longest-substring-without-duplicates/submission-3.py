'''class Solution:
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
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dic = {} # defaultdict(int)
        maxi, ptr1, ptr2 = 0, 0, 0
    
        while ptr2 < len(s):
            index = dic.get(s[ptr2], -1)
            if index != -1:
                while s[ptr1] != s[ptr2]:
                    dic[s[ptr1]] =-1
                    ptr1 +=1
                ptr1 +=1
            dic[s[ptr2]] = ptr2
            maxi = max(maxi, ptr2 - ptr1 + 1)
            ptr2 += 1

        return maxi














