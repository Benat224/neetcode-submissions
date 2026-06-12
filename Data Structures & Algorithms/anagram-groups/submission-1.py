class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        result = []
        for word in strs:
            aux = [0] * 26
            for letter in word:
                aux[ord(letter) - ord('a')] += 1
            dic[tuple(aux)].append(word)    
        return dic.values()
