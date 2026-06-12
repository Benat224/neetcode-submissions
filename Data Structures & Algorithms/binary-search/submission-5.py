class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
       

        def binary(f, l):
            if f > l:
                return -1
            m = f + (l - f) // 2
            if nums[m] < target:
                return binary(m + 1, l)
            if nums[m] > target:
                return binary(f,m - 1)
            else:
                return m
        return binary(0, len(nums) - 1)
