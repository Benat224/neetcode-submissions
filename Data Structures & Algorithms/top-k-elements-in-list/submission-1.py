class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        lista = [[] for _ in range (len(nums) + 1)]

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        for i, n in dic.items():
            lista[n].append(i)

        result = []
        for i in range(len(lista) - 1, 0, -1):
            for j in lista[i]:
                result.append(j)
                if len(result) == k:
                    return result
                
                
