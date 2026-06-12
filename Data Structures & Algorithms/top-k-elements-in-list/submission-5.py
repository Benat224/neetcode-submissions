class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapA = defaultdict(list)
        mapB = defaultdict(int)
        for val in nums:
            mapB[val] = mapB.get(val, 0) + 1
        for key, pair in mapB.items():
            mapA[pair].append(key)

        result = []
        for val in range(len(nums), 0, -1):
            while k>0 and len(mapA[val])!= 0:
                k -= 1
                aux = mapA[val].pop()
                result.append(aux)
        return result