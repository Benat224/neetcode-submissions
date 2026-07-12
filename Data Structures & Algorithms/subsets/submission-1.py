class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur = set()
        res = []
        visited = set()
        def backtracking(cur, position):
            if position == len(nums):
                if tuple(cur) not in visited:
                    res.append(list(cur))
                    visited.add(tuple(cur))
            else:
                cur.discard(nums[position])
                backtracking(cur, position + 1)
                cur.add(nums[position])
                backtracking(cur, position + 1)
        
        
            
        backtracking(cur, 0) 
        return res
            


