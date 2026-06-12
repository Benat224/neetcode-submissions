class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        return list(dic.keys())[:k]
