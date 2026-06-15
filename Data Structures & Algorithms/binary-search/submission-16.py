class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def b_search(nums:List[int], target: int, f:int, l:int)-> int:
            if l - f <= 1:
                if nums[f] == target:
                    return f
                else: 
                    return -1
            m = (l+f)//2
            print(f, m ,l)
            if nums[m] == target:
                return m
            if nums[m] < target:
                return b_search(nums, target, m, l)
            else:
                return b_search(nums, target, f, m)
        return b_search(nums, target, 0, len(nums))