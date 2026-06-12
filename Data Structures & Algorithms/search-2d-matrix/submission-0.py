class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        f, l = 0, len(matrix)* len(matrix[0]) - 1
        while f <= l:
            m = f + (l - f) // 2
            i = m // len(matrix[0])
            j = m % len(matrix[0])
            num = matrix[i][j]
            if num > target:
                l = m - 1
            elif num < target:
                f = m + 1
            else:
                return True
        return False