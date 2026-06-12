class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for j, val in enumerate(nums):
            aux = target - val
            i = dic.get(aux, -1)
            if i != -1:
                return [i, j]
            dic[val] = j