class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        col = {}
        for i in range(len(nums)):
            if target - nums[i] not in col:
                if nums[i] not in col:
                    col[nums[i]] = i
            else:
                return [col[target-nums[i]], i]
