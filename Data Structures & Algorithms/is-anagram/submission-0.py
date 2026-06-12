class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        coll = {}
        for n in s:
            if coll.get(n) == None:
                coll[n] = 1
            else:
                coll[n] += 1

        for n in t:
            if coll.get(n) == None:
                return False
            coll[n] -= 1
            if coll[n] == 0:
                coll.pop(n)

        return len(coll) == 0