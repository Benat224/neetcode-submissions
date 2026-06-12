'''class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            aux = [0] * 26
            for letter in s:
                aux[ord(letter) - ord('a')] += 1
            dic[tuple(aux)].append(s)

        return dic.values()

'''






'''class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = defaultdict(list)

        for word in strs:
            aux = ''.join(sorted(word.lower()))
            dic[aux].append(word)   

        return list(dic.values())

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            lista = [0]*26
            for letter in word:
                lista[ord(letter) -ord('a')] +=1
            dic[tuple(lista)].append(word)
        
        return dic.values()




