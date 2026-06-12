class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        col = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in col: 
                return [col[diff], i]
            col[n] = i