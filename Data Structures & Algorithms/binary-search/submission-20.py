class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def b_search(nums:List[int], target: int, f:int, l:int)-> int:
            if f == l:
                if nums[f] == target:
                    return f
                else: 
                    return -1
            m = f + (l-f)//2
            if nums[m] < target:
                return b_search(nums, target, m+1, l)
            else:
                return b_search(nums, target, f, m)
        return b_search(nums, target, 0, len(nums)-1)