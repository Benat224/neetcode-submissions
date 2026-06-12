class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        f, l = 0, len(nums) - 1
        while f <= l:
            m = f + (l - f)//2
            #m = (f + l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                l = m - 1
            else:
                f = m + 1
        return -1