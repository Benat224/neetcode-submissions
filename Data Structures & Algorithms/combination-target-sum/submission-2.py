class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        visited = set()
        res = []
        cur = []
        def dfs(i, total):
            if i == len(nums) or total>= target:
                if total == target and tuple(cur) not in visited:
                    res.append(cur.copy())
                    visited.add(tuple(cur))
                return
            counter = 0
            while nums[i]*counter + total < target:
                cur.append(nums[i])
                counter += 1
                dfs(i+1, total + nums[i]* counter)
            while counter > 0:
                cur.pop()
                counter -= 1
            dfs(i+1, total)
        
        dfs(0, 0)
        return res