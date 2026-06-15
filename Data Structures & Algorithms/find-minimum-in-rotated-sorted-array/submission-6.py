class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while r-l > 1:
            m = l + (r-l)//2
            val_l, val_m, val_r = nums[l], nums[m], nums[r]
            if val_l > val_m or val_l < val_m and val_m < val_r:
                r = m
            elif val_m > val_r:
                l = m+1
           
        
        return min(nums[l], nums[r])