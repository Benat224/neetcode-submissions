class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapA = defaultdict(list)
        for val in strs:
            aux = [0] * (ord('z') - ord('a') + 1)
            for char in val:
                aux[ord(char)-ord('a')]  += 1
            mapA[tuple(aux)].append(val)

        return list(mapA.values())