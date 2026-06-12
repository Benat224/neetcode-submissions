class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        l = [[] for _ in range(len(nums) + 1)]
        result = []
        for n in nums:
            dic[n] = dic.get(n, 0) + 1

        for n in dic:
            l[dic[n]].append(n)

        for i in range(len(l) - 1, 0, -1):
            for aux in l[i]:
                result.append(aux)
                if len(result) == k:
                    return result
        