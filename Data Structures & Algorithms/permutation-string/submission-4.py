class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0,0
        mp1, mp2 = [0]*26, [0]*26
        if len(s1) > len(s2):
            return False
        while j < len(s1):
            mp1[ord(s1[j])-ord('a')] += 1
            mp2[ord(s2[j])-ord('a')] += 1
            j += 1
        if mp1 == mp2:
            return True
        i += 1
        while j < len(s2):
            mp2[ord(s2[i-1])-ord('a')] -= 1
            mp2[ord(s2[j])-ord('a')] += 1
            print(mp1)
            print(mp2)
            if mp1 == mp2:
                return True
            i += 1
            j += 1
        return False
