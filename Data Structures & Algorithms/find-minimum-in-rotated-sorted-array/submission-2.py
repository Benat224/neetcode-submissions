class Solution:
    def findMin(self, nums: List[int]) -> int:
        f, l = 0, len(nums) - 1
        res = nums[0]
        while f <= l:
            m = (f + l) // 2
            res = min(res, nums[m])
            if nums[m] > nums[l]:
                f = m + 1
            else:
                l = m - 1
        return res