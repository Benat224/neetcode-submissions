class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        len_row =len(matrix[0])
        while l < r:
            m = l + (r-l)//2
            ml = matrix[m][0]
            mr = matrix[m][-1]
            if target > mr:
                l = m+1
            else:
                r = m
        ll, rr = 0, len_row-1
        while ll < rr:
            m = ll + (rr-ll)//2
            if matrix[l][m] < target:
                ll = m+1
            else:
                rr = m
        return matrix[l][ll] == target
















