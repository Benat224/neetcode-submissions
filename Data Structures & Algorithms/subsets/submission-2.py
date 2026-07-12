class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur = []
        res = []
        def backtracking(position):
            if position == len(nums):
                res.append(cur.copy())              
            else:
                cur.append(nums[position])
                backtracking(position + 1)
                cur.pop()
                backtracking(position + 1)
        
        
            
        backtracking(0) 
        return res
            


