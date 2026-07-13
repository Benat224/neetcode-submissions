class Solution:
    def checkIsland(self, grid, visited, i, j):
        if not (i,j) in visited:
            visited.add((i,j))
        else:
            return
        if grid[i][j]== "0":
            return
        if i != 0:
            self.checkIsland(grid, visited, i-1, j)       
        if i != len(grid)-1:
            self.checkIsland(grid, visited, i+1, j)
        if j != 0:
            self.checkIsland(grid, visited, i, j-1)
        if j != len(grid[0])-1:
            self.checkIsland(grid, visited, i, j+1)

    def numIslands(self, grid: List[List[str]]) -> int:   
        counter = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not (i,j) in visited and grid[i][j]=="1":
                    self.checkIsland(grid,visited, i, j)
                    counter += 1
        return counter