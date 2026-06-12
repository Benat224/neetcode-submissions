class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            aux = [0] * 26
            for letter in s:
                aux[ord(letter) - ord('a')] += 1
            dic[tuple(aux)].append(s)

        return dic.values()