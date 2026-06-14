class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i,j = 0,0
        visited = set()
        while j != len(s):
            char = s[j]
            if char in visited:
                while s[i]!= char:
                    visited.remove(s[i])
                    i += 1
                i += 1
            else:
                res = max(res, j-i +1)
                visited.add(char)
            j +=1
        return res