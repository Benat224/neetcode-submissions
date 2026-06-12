class Solution:
    def findMin(self, nums: List[int]) -> int:
        f, l = 0, len(nums) - 1
        while f <= l:
            if l - f <= 1:
                return min(nums[l], nums[f])
            m = (f + l) // 2
            if nums[f] < nums[l]:
                    l = m - 1
            elif nums[f] > nums[l]:
                if nums[m] < nums[f]:
                    l = m
                else:
                    f = m + 1