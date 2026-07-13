class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        maxi = 0

        def dfs(i,j, cur):
            nonlocal maxi
            
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:  
                return  cur
            
            grid[i][j] = 0
            cur += 1
            for ci, cj in directions:
                cur += dfs(i+ci, j+cj, 0)
            maxi = max(cur, maxi)
            return cur

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i,j,0)

        return maxi