class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        repeated = False
        for i in range(n):
            if nums[i] in seen:
                return  True
            else:
                seen.add(nums[i])
        return repeated    