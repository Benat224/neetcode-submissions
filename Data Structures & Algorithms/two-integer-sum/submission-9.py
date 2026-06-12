class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for j, val in enumerate(nums):
            aux = target - val
            if aux in dic:
                return [dic[aux], j]
            dic[val] = j