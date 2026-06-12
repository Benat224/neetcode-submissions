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
            for aux in mapA[val]:
                k -= 1
                result.append(aux)
                if k == 0:
                    return result
        return result