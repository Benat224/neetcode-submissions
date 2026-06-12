class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m =  len(s), len(t)
        if n != m:
            return False
        col1, col2 = {}, {}

        for i in range(n):
            col1[s[i]] = 1 + col1.get(s[i], 0)
            col2[t[i]] = 1 + col2.get(t[i], 0)

        for n in col1:
            if col1[n] != col2.get(n, 0):
                return False
        return True